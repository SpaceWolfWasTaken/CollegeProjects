 
import java.util.ArrayList;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

import java.awt.GridLayout;
import javax.swing.JComboBox;
import javax.swing.JButton;
import javax.swing.BoxLayout;
import javax.swing.Box;
import java.awt.Dimension;
import java.awt.FlowLayout;

import javax.swing.BorderFactory;
import java.awt.Color;


import java.awt.BorderLayout;

import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JOptionPane;
import javax.swing.JTabbedPane;
import java.awt.Component;

import javax.swing.JFrame;
import javax.swing.JPanel;



/**
 * Write a description of class BankGUI here.
 *
 * @author (22068176 Sujal Khatiwada)
 * @version (1.0.1)
 * 
 */
public class BankGUI
{
    private JFrame frame;
    private ArrayList<BankCard> bankCards;
    //Outer
    private JPanel topPanel, bottomPanel;
    private JTabbedPane sideTabs;
    private JLabel appTitle;
    private JButton displayBtn, clearBtn;
    //Home
    private JPanel homePanel;
    private JLabel cardIdLabel, clientNameLabel, issuerBankLabel, bankAccountLabel, balanceAmountLabel;
    private JTextField cardIdField, clientNameField, issuerBankField, bankAccountField, balanceAmountField;
    
    //Debit
    private JPanel debitPanel, makeDebitPanel, withdrawPanel;
    private JLabel pinNumberLabel, confirmPinLabel, withdrawCardIdLabel, withdrawPinLabel, withdrawAmountLabel, withdrawDateLabel;
    private JTextField pinNumberField, confirmPinField, withdrawCardIdField, withdrawPinField, withdrawAmountField;
    private JComboBox<String> withdrawDayCombo, withdrawMonthCombo, withdrawYearCombo;
    private JButton addDebitCardBtn, withdrawBtn;
    
    //Credit
    private JPanel creditPanel, makeCreditPanel, creditLimitPanel;
    private JLabel cvcNumberLabel, interestRateLabel, expirationDateLabel, creditCardIdLabel, creditLimitLabel,gracePeriodLabel;
    private JTextField cvcNumberField, interestRateField, creditCardIdField, creditLimitField, gracePeriodField;
    private JComboBox<String> expirationDayCombo, expirationMonthCombo, expirationYearCombo;
    private JButton addCreditCardBtn, setCreditLimitBtn, cancelCreditCardBtn;
    
    //For Dates
    private String[] daysArr = new String[31];
    private String[] monthsArr = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
    private String[] yearsArr = new String[44];
    
    
    BankGUI(){
        frame = new JFrame("GUI");
        frame.setSize(650,600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        bankCards = new ArrayList<BankCard>();
        
        datesArrMaker(daysArr, 1, 31);
        datesArrMaker(yearsArr, 1980, 2023);
        
        outerGUI();
        homeGUI();
        debitGUI();
        creditGUI();
        
        events();
        frame.setResizable(false);
        frame.setVisible(true);
    }
    
    public void outerGUI(){
        topPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        appTitle = new JLabel("Bank GUI");
        topPanel.add(appTitle);
        frame.add(topPanel, BorderLayout.NORTH);
        
        
        sideTabs = new JTabbedPane(JTabbedPane.LEFT, JTabbedPane.WRAP_TAB_LAYOUT);
        // sideTabs.getSelectedComponent() use this for display. potentially also for top
        frame.add(sideTabs, BorderLayout.CENTER);
        
        bottomPanel = new JPanel();
        bottomPanel.setLayout(new BoxLayout(bottomPanel, BoxLayout.LINE_AXIS));
        
        displayBtn = new JButton("Display");
        clearBtn = new JButton("Clear All");
        
        bottomPanel.add(Box.createRigidArea(new Dimension(100,0)));
        bottomPanel.add(displayBtn);
        bottomPanel.add(Box.createRigidArea(new Dimension(300,0)));
        bottomPanel.add(clearBtn);
        
        frame.add(bottomPanel, BorderLayout.SOUTH);
        
        
        
    }
    
    public void homeGUI(){
        homePanel = new JPanel();
        homePanel.setLayout(new GridLayout(7,2,0,10));
        
        
        cardIdLabel = new JLabel("Card ID: ");
        clientNameLabel = new JLabel("Client Name: ");
        issuerBankLabel = new JLabel("Issuer Bank: ");
        bankAccountLabel = new JLabel("Bank Account: ");
        balanceAmountLabel = new JLabel("Balance Amount: ");
        
        
        cardIdField = new JTextField();
        clientNameField = new JTextField();
        issuerBankField = new JTextField();
        bankAccountField = new JTextField();
        balanceAmountField = new JTextField();

        
        Component[] homeComponents = {cardIdLabel, cardIdField, clientNameLabel, clientNameField, issuerBankLabel, issuerBankField,
        bankAccountLabel, bankAccountField, balanceAmountLabel, balanceAmountField};
        
        addToPanel(homePanel, homeComponents);
        sideTabs.add("Home", homePanel);
        
    }
    
    public void debitGUI(){
        debitPanel = new JPanel();
        debitPanel.setLayout(new BoxLayout(debitPanel, BoxLayout.PAGE_AXIS));
        
        //Make Debit Content
        makeDebitPanel = new JPanel(new GridLayout(4,2,5,10));
        makeDebitPanel.setBorder(BorderFactory.createLineBorder(Color.black));
        
        
        pinNumberLabel = new JLabel("PIN Number:");
        confirmPinLabel = new JLabel("Confirm PIN:");
        
        pinNumberField = new JTextField();
        confirmPinField = new JTextField();
        
        addDebitCardBtn = new JButton("Create Card");
        
        Component[] makeDebitArr = {pinNumberLabel, pinNumberField, confirmPinLabel, confirmPinField, addDebitCardBtn};
        addToPanel(makeDebitPanel, makeDebitArr);        
        
        //Withdraw Content
        
        withdrawPanel = new JPanel(new GridLayout(6,2,5,10));
        withdrawPanel.setBorder(BorderFactory.createLineBorder(Color.black));
        
        withdrawCardIdLabel = new JLabel("Card ID:");
        withdrawPinLabel = new JLabel("PIN Number:");
        withdrawAmountLabel = new JLabel("Withdraw Amount:");
        withdrawDateLabel = new JLabel("Date of Withdrawal:");
        
        withdrawCardIdField = new JTextField();
        withdrawPinField = new JTextField();
        withdrawAmountField = new JTextField();
        
        JPanel withdrawDatePanel = new JPanel();
        withdrawDayCombo = new JComboBox<String>(daysArr);
        withdrawMonthCombo = new JComboBox<String>(monthsArr);
        withdrawYearCombo = new JComboBox<String>(yearsArr);
        
        Component[] withdrawDateArr = {withdrawDayCombo, withdrawMonthCombo,withdrawYearCombo};
        addToPanel(withdrawDatePanel, withdrawDateArr);
        
        withdrawBtn = new JButton("Withdraw");
        
        Component[] withdrawArr = {withdrawCardIdLabel,withdrawCardIdField,withdrawAmountLabel,withdrawAmountField,
            withdrawPinLabel,withdrawPinField,withdrawDateLabel,withdrawDatePanel,withdrawBtn};
        addToPanel(withdrawPanel, withdrawArr);
        
        withdrawPanel.setVisible(false);
        
        debitPanel.add(Box.createRigidArea(new Dimension(0,5)));
        debitPanel.add(makeDebitPanel);
        debitPanel.add(Box.createRigidArea(new Dimension(0,5)));
        debitPanel.add(withdrawPanel);
        debitPanel.add(Box.createRigidArea(new Dimension(0,5)));
        
        sideTabs.add("Debit Card", debitPanel);
        
    }
    
    public void creditGUI(){
        creditPanel = new JPanel();
        creditPanel.setLayout(new BoxLayout(creditPanel, BoxLayout.PAGE_AXIS));
        
        //Make Credit Content
        makeCreditPanel = new JPanel(new GridLayout(5,2,5,10));
        makeCreditPanel.setBorder(BorderFactory.createLineBorder(Color.black));
        cvcNumberLabel = new JLabel("CVC Number:");
        interestRateLabel = new JLabel("Interest Rate:");
        expirationDateLabel = new JLabel("Expiration Date:");
        
        cvcNumberField = new JTextField();
        interestRateField = new JTextField();
        
        JPanel expirationDatePanel = new JPanel();
        expirationDayCombo = new JComboBox<String>(daysArr);
        expirationMonthCombo = new JComboBox<String>(monthsArr);
        expirationYearCombo = new JComboBox<String>(yearsArr);
        
        Component[] expirationDateArr = {expirationDayCombo, expirationMonthCombo,expirationYearCombo};
        addToPanel(expirationDatePanel, expirationDateArr);
        
        addCreditCardBtn = new JButton("Create Card");
        
        Component[] makeCreditArr = {cvcNumberLabel, cvcNumberField,interestRateLabel,interestRateField,expirationDateLabel,expirationDatePanel,addCreditCardBtn};
        addToPanel(makeCreditPanel, makeCreditArr);
        
        //Credit Limit Content
                
        creditLimitPanel = new JPanel(new GridLayout(5,2,5,10));
        creditLimitPanel.setBorder(BorderFactory.createLineBorder(Color.black));
        creditCardIdLabel = new JLabel("Card ID:");
        creditLimitLabel = new JLabel("Credit Limit:");
        gracePeriodLabel = new JLabel("Grace Period:");
        
        creditCardIdField = new JTextField();
        creditLimitField = new JTextField();
        gracePeriodField = new JTextField();
        
        setCreditLimitBtn = new JButton("Set Credit Limit");
        cancelCreditCardBtn = new JButton("Cancel Credit Card");
        
        Component[] setLimitArr = {creditCardIdLabel, creditCardIdField, creditLimitLabel, creditLimitField, 
            gracePeriodLabel, gracePeriodField, setCreditLimitBtn, cancelCreditCardBtn};
        addToPanel(creditLimitPanel, setLimitArr);
        
        creditLimitPanel.setVisible(false);
        
        creditPanel.add(Box.createRigidArea(new Dimension(0,5)));
        creditPanel.add(makeCreditPanel);
        creditPanel.add(Box.createRigidArea(new Dimension(0,5)));
        creditPanel.add(creditLimitPanel);
        creditPanel.add(Box.createRigidArea(new Dimension(0,5)));
        
        sideTabs.add("Credit Card", creditPanel);
    }
    
    public void events(){
        
        addDebitCardBtn.addActionListener(new EventHandler(){
            int cardId, pinNumber, confirmPin;
            double balanceAmount;
            String clientName, issuerBank, bankAccount;
            boolean matchingCardId;
           @Override
           public void actionPerformed(ActionEvent e){               
               clientName = clientNameField.getText();
               issuerBank = issuerBankField.getText();
               bankAccount = bankAccountField.getText();
               matchingCardId = false;
               JTextField[] fieldArr = {cardIdField, balanceAmountField, pinNumberField, confirmPinField};
               
               if(areNumbers(fieldArr)){
                   cardId = Integer.parseInt(cardIdField.getText());
                   balanceAmount = Double.parseDouble(balanceAmountField.getText());
                   pinNumber = Integer.parseInt(pinNumberField.getText());
                   confirmPin = Integer.parseInt(confirmPinField.getText());
               }
               else{
                   errorMsg("Non numeric values detected on numeric fields!");
                   return;
               }
               if (pinNumber != confirmPin){
                   errorMsg("PIN Numbers don't match!");
                   return;
               }
               DebitCard debitCard = new DebitCard(balanceAmount,cardId, bankAccount, issuerBank, clientName, pinNumber);
               if (bankCards.size() == 0){
                   bankCards.add(debitCard);
                   withdrawPanel.setVisible(true);
                   return;
               }
               for (BankCard card: bankCards){
                   if (card.getCardId() == cardId){
                       matchingCardId = true;
                       errorMsg("Card ID already exists!");
                   }
               }
               if (!matchingCardId){
                   bankCards.add(debitCard);
                   withdrawPanel.setVisible(true);
                   return;
               }
            }
        });
        
        addCreditCardBtn.addActionListener(new EventHandler(){
            String clientName, issuerBank, bankAccount, expirationDate, expDay, expMonth, expYear;
            int cardId, cvcNumber;
            double balanceAmount, interestRate;
            boolean matchingCardId;
           @Override
           public void actionPerformed(ActionEvent e){
               clientName = clientNameField.getText();
               issuerBank = issuerBankField.getText();
               bankAccount = bankAccountField.getText();
               
               expDay = expirationDayCombo.getSelectedItem()+"";
               expMonth = expirationMonthCombo.getSelectedItem()+"";
               expYear = expirationYearCombo.getSelectedItem()+"";
               
               expirationDate = expDay +"-"+ expMonth +"-"+ expYear;
               
               matchingCardId = false;
               
               JTextField[] fieldArr = {cardIdField, cvcNumberField, balanceAmountField, interestRateField};
               if (areNumbers(fieldArr)){
                   cardId = Integer.parseInt(cardIdField.getText());
                   cvcNumber = Integer.parseInt(cvcNumberField.getText());
                   balanceAmount = Double.parseDouble(balanceAmountField.getText());
                   interestRate = Double.parseDouble(interestRateField.getText());
               }
               else{
                   errorMsg("Non numeric values detected on numeric fields!");
                   return;
               }
               CreditCard creditCard = new CreditCard(balanceAmount, cardId, bankAccount, issuerBank, clientName, cvcNumber, interestRate, expirationDate);
               
               if (bankCards.size() == 0){
                   bankCards.add(creditCard);
                   creditLimitPanel.setVisible(true);
                   return;
               }
               for (BankCard card: bankCards){
                   if (card.getCardId() == cardId){
                       matchingCardId = true;
                       errorMsg("Card ID already exists!");
                       return;
                   }
               }
               if (!matchingCardId){
                   bankCards.add(creditCard);
                   creditLimitPanel.setVisible(true);
                   return;
               }
            }
        });
        
        withdrawBtn.addActionListener(new EventHandler(){
            String dateOfWithdrawal, withDay, withMonth, withYear;
            int cardId, withdrawalAmount, pinNumber;
           @Override
           public void actionPerformed(ActionEvent e){
               withDay = withdrawDayCombo.getSelectedItem()+"";
               withMonth = withdrawMonthCombo.getSelectedItem()+"";
               withYear = withdrawYearCombo.getSelectedItem()+"";
               
               dateOfWithdrawal = withDay+"-"+withMonth+"-"+withYear;
               int confirmWithdraw;
               JTextField[] withdrawFieldArr = {withdrawAmountField,withdrawPinField,withdrawCardIdField};
               if (areNumbers(withdrawFieldArr)){
                   withdrawalAmount = Integer.parseInt(withdrawAmountField.getText());
                   pinNumber = Integer.parseInt(withdrawPinField.getText());
                   cardId = Integer.parseInt(withdrawCardIdField.getText());
               } else{
                   errorMsg("The information you have provided contain alphabets or spaces.");
                   return;
               }
               String msg = "You have given the following values for withdrawal:\n"+
               "Card ID: " + cardId+"\n"+
               "PIN Number: " + pinNumber + "\n" +
               "Withdrawal Amount: " + withdrawalAmount + "\n" +
               "Date of Withdrawal: " + dateOfWithdrawal + "\n" +
               "Confirm?";
               
               confirmWithdraw = JOptionPane.showConfirmDialog(frame, msg);
               if (confirmWithdraw == JOptionPane.YES_OPTION){
                   for (BankCard card: bankCards){
                       if(card instanceof DebitCard){
                           if (card.getCardId() == cardId){
                               DebitCard dCard = (DebitCard)card;
                               if (dCard.getBalanceAmount() < withdrawalAmount){
                                   errorMsg("Withdrawal amount greater than your balance.");
                                   return;
                               }else{
                                   dCard.withdraw(withdrawalAmount, dateOfWithdrawal, pinNumber);
                                   String withdrawMsg = ""+withdrawalAmount+" has been successfully withdrawn\n"+
                                   "from " +cardId+ ".";
                                   infoMsg(withdrawMsg, "Success");
                                   return;
                               }
                           }
                           
                       }
                    }
                    errorMsg("Card ID doesn't exist.");
                    
               } else{
                   infoMsg("Cancelled", "Withdraw");
                   return;
               }
               
               
           }
        });
        
        setCreditLimitBtn.addActionListener(new EventHandler(){
            double creditLimit;
            int cardId, gracePeriod, confirmSetLimit;
           @Override
           public void actionPerformed(ActionEvent e){
               JTextField[] setLimitArr = {creditLimitField, creditCardIdField, gracePeriodField};
               if (areNumbers(setLimitArr)){
                   creditLimit = Double.parseDouble(creditLimitField.getText());
                   cardId = Integer.parseInt(creditCardIdField.getText());
                   gracePeriod = Integer.parseInt(gracePeriodField.getText());
               } else{
                   errorMsg("The information you have provided contain alphabets or spaces.");
                   return;
               }
               
               String msg = "You have given the following values for credit limit:\n"+
               "Card ID: "+cardId +"\n"+
               "Credit Limit: " + creditLimit + "\n"+
               "Grace Period: " + gracePeriod +"\n"+
               "Confirm?";
               confirmSetLimit = JOptionPane.showConfirmDialog(frame, msg);
               if (confirmSetLimit == JOptionPane.YES_OPTION){
                   for (BankCard card: bankCards){
                       if(card instanceof CreditCard ){
                           if (card.getCardId() == cardId){
                               CreditCard cCard = (CreditCard)card;
                               if(creditLimit <= 2.5 * cCard.getBalanceAmount()){
                                   cCard.setCreditLimit(creditLimit, gracePeriod);
                                   String setLimitMsg = "Credit limit of "+creditLimit + " has been set for the card " + cardId +
                                   " with a grace period of "+gracePeriod + ".";
                                   infoMsg(setLimitMsg, "Success");
                                   return;
                               } else{
                                   errorMsg("The specified credit limit is more than what is available for your account.");
                                   return;
                               }
                            }
                       }
                    }
                    errorMsg("Card ID doesn't exist.");
                    
               } else{
                   infoMsg("Cancelled", "Set Credit Limit");
                   return;
               }
           }
        });
        
        cancelCreditCardBtn.addActionListener(new EventHandler(){
           @Override
           public void actionPerformed(ActionEvent e){
               int intCardId;
               String inputCardId = JOptionPane.showInputDialog(frame, "Card ID: ");
               if(isANumber(inputCardId)){
                   intCardId = Integer.parseInt(inputCardId);
               }else{
                   errorMsg("Enter a numeric value!");
                   return;
               }
               for (BankCard card: bankCards){
                       if(card instanceof CreditCard){
                           if (card.getCardId() == intCardId){
                               CreditCard cCard = (CreditCard)card;
                               cCard.cancelCreditCard();
                               infoMsg("Your credit card has been cancelled.", "Cancel Card");
                               return;
                            }
                       }
                    }
                    errorMsg("Card ID doesn't exist.");
                    
               
           }
        });
        
        displayBtn.addActionListener(new EventHandler(){
            @Override
            public void actionPerformed(ActionEvent e){
                String inputCardId = JOptionPane.showInputDialog(frame, "Card ID: ", "Entering non numerical vaues will display all.");
                int tabIndex = sideTabs.getSelectedIndex();
                String currentTab = sideTabs.getTitleAt(tabIndex);
                int intCardId;
                
                if(!isANumber(inputCardId)){
                    if (currentTab == "Home"){
                        errorMsg("Cannot display content while on Home tab.\n Go to Debit Card or Credit Card tabs and click on the display button.");
                    }
                    else if (currentTab == "Debit Card"){
                        for (BankCard card: bankCards){
                            if (card instanceof DebitCard){
                                DebitCard dCard = (DebitCard) card;
                                dCard.display();
                                System.out.println("\n");
                            }
                        }
                    }
                    else if (currentTab == "Credit Card"){
                        for (BankCard card: bankCards){
                            if (card instanceof CreditCard){
                                CreditCard cCard = (CreditCard) card;
                                cCard.display();
                                System.out.println("\n");
                            }
                        }
                    }
                    return;    
                }else{
                intCardId = Integer.parseInt(inputCardId);
                for (BankCard card:bankCards){
                    if(card.getCardId() == intCardId){
                        if (card instanceof DebitCard){
                            DebitCard dCard = (DebitCard) card;
                            dCard.display();
                            System.out.println("\n");
                            return;
                            }
                        if (card instanceof CreditCard){
                            CreditCard cCard = (CreditCard) card;
                            cCard.display();
                            System.out.println("\n");
                            return;
                            }
                    }
                }
                errorMsg("No card in our database has that Card ID.");
            }
                
                
            }
        });
        
        clearBtn.addActionListener(new EventHandler(){
            @Override            
            public void actionPerformed(ActionEvent e){
                JTextField[] fieldArr = {cardIdField, clientNameField, issuerBankField, bankAccountField, balanceAmountField,
                pinNumberField, confirmPinField, withdrawCardIdField, withdrawPinField, withdrawAmountField, 
                cvcNumberField, interestRateField, creditCardIdField, creditLimitField, gracePeriodField};
            
                for(JTextField field: fieldArr){
                    field.setText("");
                }
            }
        });
    }
    
    public void addToPanel(JPanel panel, Component[] array){
        for (Component comp: array){
            panel.add(comp);
        }
    }
    
    public boolean isANumber(String number){
        try{
            double checkNum = Double.parseDouble(number); //Returns true for both integers and doubles
            return true;
        }catch(NumberFormatException ex){
            return false;
        }catch(NullPointerException ex){
            return false;
        }
    }
    
    public boolean areNumbers(JTextField[] array){
        try{
            for (JTextField field: array){
                double checkNum = Double.parseDouble(field.getText());
            }
        } catch(NumberFormatException ex){
            return false;
        }catch(NullPointerException ex){
            return false;
        }
        return true;
    }
    
    public void datesArrMaker(String[] arr, int start, int stop){
        int index = 0;
        for(int i = start; i <= stop; i++){
            arr[index] = i+"";
            index++;
        }
    }
    public void errorMsg(String msg){
        JOptionPane.showMessageDialog(frame, msg, "Error", JOptionPane.ERROR_MESSAGE);
    }
    public void infoMsg(String msg, String heading){
        JOptionPane.showMessageDialog(frame, msg, heading, JOptionPane.INFORMATION_MESSAGE);
    }
    public static void main(String[] args){
        new BankGUI();
        
    }
    
    public class EventHandler implements ActionListener{
        @Override
        public void actionPerformed(ActionEvent e){
            
        }
    }
}
