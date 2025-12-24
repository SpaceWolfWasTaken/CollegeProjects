 
/**
 * Write a description of class BankCard here.
 *
 * @author (22068176 Sujal Khatiwada)
 * @version (1.0.0)
 */
public class BankCard
{
    //Attributes for the class
    private int cardId;
    private String clientName;
    private String issuerBank;
    private String bankAccount;
    private double balanceAmount;
    
    //Constructor
    public BankCard(double balanceAmount, int cardId, String bankAccount, String issuerBank)
    {
        this.clientName = "";
        this.balanceAmount = balanceAmount;
        this.cardId = cardId;
        this.bankAccount = bankAccount;
        this.issuerBank = issuerBank;
    }
    
    //Methods
   
    //Accessor Methods
    public int getCardId()
    {
        return this.cardId;
    }
    
    public String getIssuerBank()
    {
        return this.issuerBank;
    }
    
    public String getBankAccount()
    {
        return this.bankAccount;
    }
    
    public double getBalanceAmount()
    {
        return this.balanceAmount;
    }
    
    public String getClientName()
    {
        return this.clientName;
    }
    //Accessor Method End

    //Method to set Balance Amount
    public void setBalanceAmount(double balanceAmount)
    {
        this.balanceAmount = balanceAmount;
    }
    
    //Method to set Client Name
    public void setClientName(String clientName)
    {
        this.clientName = clientName;
    }
    
    //Display Information
    public void display()
    {
        System.out.println("Your Card ID is: " + cardId + ".");
        //Check clientName and display suitable information
        if (clientName == "")
        {
            System.out.println("Client name has not been assigned.");
        }
        else
        {
            System.out.println("Client name is: " + clientName + ".");
        }
        System.out.println("Your Issuer bank is: " + issuerBank + ".");
        System.out.println("Your Bank account is: " + bankAccount + ".");
        System.out.println("Your Balance Amount is: " + balanceAmount +".");
    }
}
