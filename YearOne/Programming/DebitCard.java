 

/**
 * Write a description of class DebitCard here.
 *
 * @author (22068176 Sujal Khatiwada)
 * @version (1.0.0)
 */
public class DebitCard extends BankCard
{
    //Class Attributes
    private int pinNumber;
    private int withdrawalAmount;
    private String dateOfWithdrawal;
    private boolean hasWithdrawn;
    
    //Constructor
    public DebitCard(double balanceAmount, int cardId, String bankAccount, String issuerBank, String clientName, int pinNumber)
    {
        super(balanceAmount, cardId, bankAccount, issuerBank);
        super.setClientName(clientName);
        this.pinNumber = pinNumber;
        this.hasWithdrawn = false;
        
    }
    
    //Methods
    //Accessor Methods
    public int getPinNumber()
    {
        return this.pinNumber;
    }
    
    public int getWithdrawalAmount()
    {
        return this.withdrawalAmount;
    }
    
    public String getDateOfWithdrawal()
    {
        return this.dateOfWithdrawal;
    }
    
    public boolean getHasWithdrawn()
    {
        return this.hasWithdrawn;
    }
    
    //Accessor Method End
    
    //Mutator Method to set new Withdrawal Amount
    public void setWithdrawalAmount(int withdrawalAmount)
    {
        this.withdrawalAmount = withdrawalAmount;
    }
    
    //Method to deduct money from client account
    public void withdraw(int withdrawalAmount, String dateOfWithdrawal, int pinNumber)
    {
        if (pinNumber == this.pinNumber) //Checks if pin number  matches.
        {
            if(withdrawalAmount <= super.getBalanceAmount()) //Compares withdrawal amount with balance amount.
            {
                if(withdrawalAmount > 0) //checks if withdrawal amount is more than 0.
                {
                    this.hasWithdrawn = true;
                    this.dateOfWithdrawal = dateOfWithdrawal;
                    this.withdrawalAmount = withdrawalAmount;
                    double newBalance = super.getBalanceAmount() - withdrawalAmount;
                    super.setBalanceAmount(newBalance);
                }
                else //displays only if withdrawal amount is 0 or less.
                {
                    System.out.println("No amount has been withdrawn.\n Your balance is: " + super.getBalanceAmount() + ".");
                }
            }
            else
            {
                System.out.println("Error! Withdrawal amount is greater than your balance.");
            }
            
        }
        else
        {
            System.out.println("Error! Wrong PIN detected.");
        }
        
        
    }
    
    //Method to display card data
    
    public void display()
    {
        super.display();  //Calls display() from superclass.
        if (this.hasWithdrawn == true) // Checks if amount has been withdrawn from balance.
        {
            System.out.println("Your PIN Number is: " + this.pinNumber + ".");
            System.out.println("The date of your withdrawal is: " + this.dateOfWithdrawal + ".");
            System.out.println("Your withdrawal amount is: " + this.withdrawalAmount + ".");
            
        }
    }

} 

