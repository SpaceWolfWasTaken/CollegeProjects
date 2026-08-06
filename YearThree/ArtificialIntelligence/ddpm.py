from diffusers import UNet2DModel
from diffusers import DDPMScheduler, DDPMPipeline
from diffusers.utils import make_image_grid
import os
import torch
import torch.nn.functional as F
from accelerate import Accelerator
from tqdm.auto import tqdm
from diffusers.optimization import get_cosine_schedule_with_warmup
from accelerate import notebook_launcher


class DDPM:
    def __init__(self, config):
        self.config = config
        self.model = self.model_init()
        self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=config.learning_rate)
        self.noise_scheduler = DDPMScheduler(num_train_timesteps=1000)            

    def evaluate(self, epoch, pipeline):
        # Sample some images from random noise (this is the backward diffusion process).
        # The default pipeline output type is `List[PIL.Image]`
        images = pipeline(
            batch_size=self.config.eval_batch_size,
            generator=torch.Generator(device='cpu').manual_seed(self.config.seed), # Use a separate torch generator to avoid rewinding the random state of the main training loop
        ).images

        # Make a grid out of the images
        image_grid = make_image_grid(images, rows=4, cols=4)

        # Save the images
        test_dir = os.path.join(self.config.output_dir, "samples")
        os.makedirs(test_dir, exist_ok=True)
        image_grid.save(f"{test_dir}/{epoch:04d}.png")

    def train_loop(self, train_dataloader, lr_scheduler):
        # Initialize accelerator and tensorboard logging
        accelerator = Accelerator(
            mixed_precision=self.config.mixed_precision,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            log_with="tensorboard",
            project_dir=os.path.join(self.config.output_dir, "logs"),
        )
        if accelerator.is_main_process:
            if self.config.output_dir is not None:
                os.makedirs(self.config.output_dir, exist_ok=True)
            accelerator.init_trackers("train_example")

        model, optimizer, train_dataloader, lr_scheduler = accelerator.prepare(
            self.model, self.optimizer, train_dataloader, lr_scheduler
        )

        global_step = 0

        for epoch in range(self.config.num_epochs):
            progress_bar = tqdm(total=len(train_dataloader), disable=not accelerator.is_local_main_process)
            progress_bar.set_description(f"Epoch {epoch}")

            for step, batch in enumerate(train_dataloader):
                clean_images = batch["images"]
                # Sample noise to add to the images
                noise = torch.randn(clean_images.shape, device=clean_images.device)
                bs = clean_images.shape[0]

                # Sample a random timestep for each image
                timesteps = torch.randint(
                    0, self.noise_scheduler.config.num_train_timesteps, (bs,), device=clean_images.device,
                    dtype=torch.int64
                )

                # Add noise to the clean images according to the noise magnitude at each timestep
                # (this is the forward diffusion process)
                noisy_images = self.noise_scheduler.add_noise(clean_images, noise, timesteps)

                with accelerator.accumulate(model):
                    # Predict the noise residual
                    noise_pred = model(noisy_images, timesteps, return_dict=False)[0]
                    loss = F.mse_loss(noise_pred, noise)
                    accelerator.backward(loss)

                    if accelerator.sync_gradients:
                        accelerator.clip_grad_norm_(model.parameters(), 1.0)
                    optimizer.step()
                    lr_scheduler.step()
                    optimizer.zero_grad()

                progress_bar.update(1)
                logs = {"loss": loss.detach().item(), "lr": lr_scheduler.get_last_lr()[0], "step": global_step}
                progress_bar.set_postfix(**logs)
                accelerator.log(logs, step=global_step)
                global_step += 1

            if accelerator.is_main_process:
                pipeline = DDPMPipeline(unet=accelerator.unwrap_model(model), scheduler=self.noise_scheduler)

                if (epoch + 1) % self.config.save_image_epochs == 0 or epoch == self.config.num_epochs - 1:
                    self.evaluate(epoch, pipeline)

                if (epoch + 1) % self.config.save_model_epochs == 0 or epoch == self.config.num_epochs - 1:
                    pipeline.save_pretrained(self.config.output_dir)

    def fit(self, train_dataloader):
        lr_scheduler = get_cosine_schedule_with_warmup(
            optimizer=self.optimizer,
            num_warmup_steps=self.config.lr_warmup_steps,
            num_training_steps=(len(train_dataloader) * self.config.num_epochs),
        )

        args = (train_dataloader, lr_scheduler)

        notebook_launcher(self.train_loop, args, num_processes=1)

    def model_init(self):
        return UNet2DModel(
            sample_size=self.config.image_size,  # the target image resolution
            in_channels=3,  # the number of input channels, 3 for RGB images
            out_channels=3,  # the number of output channels
            layers_per_block=2,  # how many ResNet layers to use per UNet block
            block_out_channels=(128, 128, 256, 256, 512, 512),  # the number of output channels for each UNet block
            down_block_types=(
                "DownBlock2D",  # a regular ResNet downsampling block
                "DownBlock2D",
                "DownBlock2D",
                "DownBlock2D",
                "AttnDownBlock2D",  # a ResNet downsampling block with spatial self-attention
                "DownBlock2D",
            ),
            up_block_types=(
                "UpBlock2D",  # a regular ResNet upsampling block
                "AttnUpBlock2D",  # a ResNet upsampling block with spatial self-attention
                "UpBlock2D",
                "UpBlock2D",
                "UpBlock2D",
                "UpBlock2D",
            ),
        )