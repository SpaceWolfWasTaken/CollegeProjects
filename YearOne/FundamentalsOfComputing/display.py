#display module. Contains user interactions

SIZE = 90
dict_ = dict()
keys = tuple()
def path(): print("#"*SIZE)

def intro():
    path()
    print("\t\t\tHello.\tWelcome to the laptop shop!!")
    path()

def request_cust_type():
    while True:
        cust_type =  input("Are you joining in as a customer or supplier/manufacturer? ")
        cust_type = cust_type.lower()
        customers = ("customer","supplier","manufacturer","admin","bye")
        if cust_type in customers:
            return cust_type 
        else:
            print("Enter the correct prompt!")

def request_client_name(cust_type) -> str:
    path()
    if cust_type == "customer":
        client_name = input("\t\t What is your respected name? ")
    if cust_type == "supplier" or cust_type == "manufacturer":
        client_name = input("\t\t What company are you representing? ")
    return client_name

def showProducts():
    line = "-"*89
    print(line)
    print("|ID | Name\t\t\t|  GPU \t\t|  CPU\t\t| Amount   | Price\t|")
    print(line)
    for index_ in range(len(dict_["Name"])):
        gap_name = "\t"
        gap_gpu = "\t"
        gap_cpu = "\t"
        name_ = dict_["Name"][index_]
        gpu_ = dict_["GPU"][index_]
        cpu_ = dict_["CPU"][index_]

        #gap_name
        if len(name_) <= 9:
            gap_name = "\t\t\t"
        elif len(name_) <= 14:
            gap_name = "\t\t"

        if len(gpu_) <=8:
            gap_gpu = "\t\t"
        
        if len(cpu_) <= 9:
            gap_cpu = "\t\t"

        print("|"+str(index_+1)+". | ", end="")
        print(dict_["Name"][index_] + gap_name, end = "| ")
        #add \t gap in gpu and cpu depending on len
        print(str(dict_["GPU"][index_]), end = gap_gpu+"| ")
        print(str(dict_["CPU"][index_]), end = gap_cpu+"| ")
        print(str(dict_["Amount"][index_]), end = "\t   | ")
        print("$"+str(dict_["Price"][index_]) + "\t", end = "|\n"+line+"\n")
        
#validation (>0...) done by calling another method
def requestProduct(cust_type):
    if cust_type == "customer": 
        product_id = input("What product would you like to buy? ")
    if cust_type == "supplier" or cust_type == "manufacturer":
        product_id = input("What product would you like us to stock up? ")
    try:
        product_id = int(product_id)
    except ValueError:
        print("Enter valid ID!")
        return False
    return product_id

#validation done in another method
def requestAmount(cust_type):
    if cust_type == "customer": 
        product_amt = input("How many of it would you like to buy? ")
    if cust_type == "supplier" or cust_type == "manufacturer":
        product_amt = input("How many of it would you like us to stock up? ")
    try:
        product_amt = int(product_amt)
    except ValueError:
        print("Enter a number!")
        return False
    return product_amt
    
def ask_shipping() -> bool:
    while True:
        ask_ = input("Would you like us to ship the products (Y/N)? ").lower()
        if ask_ == "y" or ask_ == "yes":
            return True
        if ask_ == "n" or ask_ == "no":
            return False
        print("Enter the correct prompt!")

def ask_more_items(customer_type) -> bool:
    to_do = ""
    if customer_type == "customer":
        to_do = "buy"
    else:
        to_do = "sell"
    while True:
        ask_ = input("Would you like to "+ to_do +" more products (Y/N)? ").lower()
        if ask_ == "y" or ask_ == "yes":
            return True
        if ask_ == "n" or ask_ == "no":
            return False
        print("Enter the correct prompt!")

def admin_pw(de_encrypted_password):
    for i in range(4):
        password = input("Enter password: ")
        if len(password) > 8:
            print("Error!You have " + str(3-i) +" tries left!")
            continue
        try:
            password = int(password)
        except:
            print("Error!You have " + str(3-i) +" tries left!")
            continue
        if password == de_encrypted_password:
            return True
        else:
            print("Error!You have " + str(3-i) +" tries left!")
    else:
        print("You have failed to login! \n Quitting...")
    return False

def admin_help():
    print("Hello admin! As a root user, you are allowed the following commands:\
          \nADD: Adds a product\
          \nREMOVE: Removes a product\
          \nSHOW: Shows the current list of products\
          \nUPDATE: Updates the stock file\
          \nHELP: Shows the list of commands\
          \nQUIT: Quits admin mode.")
    
def admin_ask(commands):
    while True:
        ask_command = input("What would you like to do? ")
        if ask_command in commands:
            return ask_command
        print("Enter the correct command! Commands are case sensitive")

    

#they will only take input and return values.
#actual changes will occur in compute
def add_product():
    '''
    Takes multiple input for adding product
    '''
    product_name = input("Enter the product's name: ")
    product_company = input("Enter the company's name: ")
    while True:
        product_price = input("Enter the product's price: $")
        try:
            product_price = int(product_price)
        except:
            print("Enter a number!")
            continue
        if product_price > 0:
            break
        print("Enter an amount greater than 0")
    while True:
        product_amount = input("Enter the amount of product: ")
        try:
            product_amount = int(product_amount)
        except:
            print("Enter a number!")
            continue
        if product_amount > 0:
            break
        print("Enter an amount greater than 0")
    product_cpu = input("Enter the product's CPU architecture: ")
    product_gpu = input("Enter the product's GPU architecture: ")
    return product_name, product_company, product_price, product_amount, product_cpu, product_gpu
        

def remove_product():
    '''
    Display table. get id and remove product
    '''
    showProducts()
    while True:
        remove_product_var = input("What product would you like to remove? ")
        try:
            remove_product_var = int(remove_product_var)
            if remove_product_var > 0 or remove_product_var <= len(dict_["Name"]):
                return remove_product_var - 1
            print("Enter the product id present in the table!")
        except:
            print("Enter a number!")
            





        

        


        

