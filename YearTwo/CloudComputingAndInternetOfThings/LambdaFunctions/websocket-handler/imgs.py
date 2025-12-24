

def add_image(s3_resource, buffer):
    #overrides image.
    s3_bucket = s3_resource.Bucket(name='iotdatasc')
    s3_bucket.put_object(
        Key='image.jpeg',
        Body=buffer
    )
