#main module
#reference all dict_ and keys in other modules to the dictionary and tuple in data module
import read
import compute as comp
import data	
import display as dsp
import write as wr
import add_product as ap
import datetime as dt
import encrypt as enc

stock_dict = data.data_dict
dict_keys = data.keys

modules = (read, comp, dsp, wr, ap)
for module_ in modules:
    module_.dict_ = stock_dict
    module_.keys = dict_keys


def main():

    #initializing
    date_ = dt.datetime.now()
    #Takes the current date in DD-MM-YYYY
    current_date = date_.strftime("%d-%m-%Y")
    wr.make_invoice_folder(current_date)
    read.read_file()
    while True:

        #initializing
        shipping_flag = False
        products = []
        amounts = []

        dsp.intro()
        customer_type = dsp.request_cust_type()
        if customer_type == "bye":
            print("Goodbye!")
            break
        if customer_type == "admin":
            password = enc.deencrypt(data.password)
            if dsp.admin_pw(password):
                dsp.admin_help()
                while True:
                    command = dsp.admin_ask(data.commands)
                    if command == "ADD":
                        ap.ap2(dsp.add_product())
                    elif command == "REMOVE":
                        ap.remove_product(dsp.remove_product())
                    elif command == "UPDATE":
                        wr.write_to_stock()
                        print("Stock updated!")
                    elif command == "HELP":
                        dsp.admin_help()
                    elif command == "SHOW":
                        dsp.showProducts()
                    else:
                        print("Quitting...")
                        break
            break #breaks the main loop
        customer_name = dsp.request_client_name(customer_type)
        while True:
            print("\n")
            dsp.showProducts()
            print("\n")

            product_id = dsp.requestProduct(customer_type)
            while product_id == False:
                product_id = dsp.requestProduct(customer_type)
                if comp.check_item(product_id) == False:
                    print("Enter valid ID!")
                    product_id = False

            product_amount = dsp.requestAmount(customer_type)
            while product_amount == False:
                product_amount = dsp.requestAmount(customer_type)
                if comp.check_buyable(product_id, product_amount) == False:
                    product_amount = False
                    print("Enter valid Amount!")
            
            products.append(product_id)
            amounts.append(product_amount)
            comp.inventory_change(customer_type, product_id, product_amount)

            if dsp.ask_more_items(customer_type) == True: 
                continue  

            if customer_type == "customer":
                shipping_flag = dsp.ask_shipping()
            print("Generating bill...")
            invoice_time = date_.strftime("%H:%M:%S")

            wr.invoice_make(customer_type, customer_name, products, amounts, current_date, invoice_time,shipping_flag)
            wr.write_to_stock()    
            print("Thank you for shopping here!\n\n")
            break        
        

if __name__ == "__main__":
    main()