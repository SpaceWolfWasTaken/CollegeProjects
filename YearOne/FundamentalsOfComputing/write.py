#write module
import os

#writes data

dict_ = dict()
keys = tuple()

def make_invoice_folder(current_date):
    '''
    Makes folders for customer and manufacturer with name as the current date, if they don't exist.
    '''
    dir_cust = ".\\Invoice\\Customer\\"+current_date
    dir_manfac = ".\\Invoice\\Manufacturer\\"+current_date

    #checks if folder exists in customer folder
    if not os.path.exists(dir_cust):
        os.mkdir(dir_cust)
        print("Customer Directory made!") # for testing
    else:
        #else block also for testing. un-needed in actual program
        print("Customer Directory already exists!")
    
    #checks if folder exists in manufacturer folder
    if not os.path.exists(dir_manfac):
        os.mkdir(dir_manfac)
        print("Manufacturer Directory made!") # for testing
    else:
        #else block also for testing. un-needed in actual program
        print("Manufacturer Directory already exists!")

def write_to_stock(file_name = "stock.txt"):
    '''
    Takes a filename as argument. This function reads through the data in the stock dictionary and writes it to a text file.
    '''
    file_dir = ".\\Stock\\"+file_name
    #clears file
    file_ = open(file_dir, "w")
    file_.close()

    #initializing lists to eventually store data from dictionary, and to file.
    list_from_dict = []

    #append data to file
    with open(file_dir, "a") as stock_file:
        for index_ in range(len(dict_["Name"])): #gets an increasing value for the amount of elements in name of dictionary
            for key in keys: #loops through all keys in the tuple.
                if key == "Price":
                    list_from_dict.append("$"+str(dict_[key][index_]).strip())
                    continue
                list_from_dict.append(str(dict_[key][index_]).strip()) #strip removes white spaces
            stock_file.write(str(list_from_dict).replace("[", "").replace("]", "").replace("'", ""))
            stock_file.write("\n")
            list_from_dict.clear() #clearing list for new iteration
        
        del list_from_dict #deleting list to save memory

def invoice_make(client_type, client_name, products, amounts, current_date, invoice_time,shipping_cost_flag = False):
    client = ""
    grand_total_text = ""
    table_print = ""
    folder_name = ""
    total = 0

    if client_type == "supplier" or client_type =="manufacturer":
        client = "Distributor"
    if client_type == "customer":
        client = "Customer"

    to_print = client+" Name: " + client_name + "\n" + \
            "Date of Purchase: " + current_date + "\n" \
            "Time of Purchase: " + invoice_time + "\n\n"
    

    
    if len(products) == 1:
        index_ = 0
        data_index = products[index_] - 1
        product_name = dict_["Name"][data_index]
        brand_name = dict_["Company"][data_index]
        price_ = dict_["Price"][data_index]
        amount_ = amounts[index_]
        individual_total = price_ * amount_
        total += individual_total

        to_add = \
        "Laptop Name: " + product_name + "\n" + \
        "Brand Name: " + brand_name + "\n" + \
        "No. of items: " + str(amount_) + "\n" + \
        "Price: $" + str(individual_total) + "\n\n"

        to_print += to_add
    else:

        #make table
        line = "-"*79 + "\n"
        table_print = line + \
        "|ID | Name\t\t\t| Company\t\t| Amount    | Price\t| Total \t|\n" + \
        line
        
        
        for index_ in range(len(products)):
            name_gap = "\t"
            brand_gap = "\t"
            total_gap = "\t"
            data_index = products[index_] - 1
            product_name = dict_["Name"][data_index]
            brand_name = dict_["Company"][data_index]
            price_ = dict_["Price"][data_index]
            amount_ = amounts[index_]
            individual_total = price_ * amount_

            if len(product_name) <=4:
                name_gap = "\t\t\t"
            elif len(product_name) <= 11: #do something for razer blade. was 9. set to 11 for test
                name_gap = "\t\t"
            elif len(product_name) <= 14:
                name_gap = "\t"
            else:
                pass

            if len(brand_name) <= 6:
                brand_gap = "\t\t"
            '''
            if individual_total < 10000:
                total_gap = "\t\t"
            '''

            table_print += \
            "|"+str(index_+1)+". | " + \
            product_name + name_gap +  "| "+ \
            brand_name+ brand_gap + "| " + \
            str(amount_) + " \t\t|" + \
            " $"+str(price_) + "\t" + "| " + \
            "$"+str(individual_total) + total_gap+"|\n"+line

            total += individual_total
        to_print += table_print

    if client_type == "customer":
        folder_name = "Customer"
        if shipping_cost_flag == True:
            grand_total_text = \
            "Total Amount without shipping: $" + str(total) + "\n" + \
            "Shipping Cost: $50" + "\n" + \
            "Total Amount: $" + str(total+50)

        else:
            grand_total_text = "Total Amount: $" + str(total)

    if client_type == "supplier" or client_type =="manufacturer":
        folder_name = "Manufacturer"

        grand_total_text = "Net Amount: $" + str(total) + "\n" + \
            "Applicable VAT Amount: $" + str(0.13 * total) + "\n" + \
            "Gross Amount: $" + str(total + 0.13 * total) + "\n"

    file_name_time = invoice_time.replace(":","-")
    dir_ = ".\\Invoice\\"+folder_name+"\\" + current_date + "\\"+ file_name_time+ "-" + client_name + ".txt"
    with open(dir_, 'w') as file_:
        file_.write(to_print)
        file_.write(grand_total_text)
    
    

        

    