 
/**
 * Write a description of class CreditCard here.
 *
 * @author (22068176 Sujal Khatiwada)
 * @version (1.0.0)
 */
public class CreditCard extends BankCard
{
    //Class Attributes
    private int cvcNumber;
    private double creditLimit;
    private double interestRate;
    private String expirationDate;
    private int gracePeriod;
    private boolean isGranted;
    
    //Constructor
    public CreditCard(double balanceAmount, int cardId, String bankAccount, String issuerBank, String clientName, int cvcNumber, double interestRate, String expirationDate)
    {
        super(balanceAmount, cardId, bankAccount, issuerBank);
        super.setClientName(clientName);
        this.cvcNumber = cvcNumber;
        this.interestRate = interestRate;
        this.expirationDate = expirationDate;
        this.isGranted = false; //flag for credit granting
    }
    
    //Class Methods
    
    //Accessor Methods
    
    public int getCvcNumber()
    {
        return this.cvcNumber;
    }
    
    public double getCreditLimit()
    {
        return this.creditLimit;
    }
    
    public double getInterestRate()
    {
        return this.interestRate;
    }
    
    public String getExpirationDate()
    {
        return this.expirationDate;
    }
    
    public int getGracePeriod()
    {
        return this.gracePeriod;
    }
    
    public boolean getIsGranted()
    {
        return this.isGranted;
    }

    //Method to set credit limit
    public void setCreditLimit(double creditLimit, int gracePeriod)
    {
        if (creditLimit <= super.getBalanceAmount() * 2.5)
        {
            this.creditLimit = creditLimit;
            this.gracePeriod = gracePeriod;
            this.isGranted = true; //flag(true) for credit granting
        }
        else
        {
            System.out.println("Credit cannot be issued.");
        }
    }
    
    //Method to cancel the credit card.
    public void cancelCreditCard()
    {   
            this.cvcNumber = 0;
            this.creditLimit = 0;
            this.gracePeriod = 0;
            this.isGranted = false;
    }
    
    //method to display credit card
    public void display()
    {
        super.display(); //Calls display() from superclass.
        System.out.println("Your CVC number is:" + this.cvcNumber + ".");
        System.out.println("Your interest rate is: " + this.interestRate + ".");
        System.out.println("Your expiration date for the card is: " + this.expirationDate + ".");
            
        if (this.isGranted == true) //Checks if credit has been granted.
        {
            System.out.println("Your Credit limit is: " + this.creditLimit + ".");
            System.out.println("Your grace period for paying back is: " + this.gracePeriod + ".");            
        }
        
    }
       
}
