#test module

import data
import read
import add_product as ap
import writeTwo
import display

import compute

read.dict_ = data.data_dict
read.keys = data.keys

compute.dict_ = data.data_dict

writeTwo.dict_ = data.data_dict
writeTwo.keys = data.keys

ap.dict_ = data.data_dict
ap.keys = data.keys

display.keys = data.keys
display.dict_ = data.data_dict


read.read_file()

'''
display.showProducts()

client_type = "supplier"
client_name = "Acer"
products = [2,3,1]
amounts = [10,10,20]
current_date = "21-21-03"
invoice_time = "time"

writeTwo.invoice_make(client_type, client_name, products, amounts, current_date, invoice_time,shipping_cost_flag = False)


name_client = "Sujal"
products = ("XPS", "Alienware")
amounts = (5 , 6)

name_manufac = "Asdasd"

#both works. merge both functions later?

write.invoice_customer(name_client, products, amounts, True, "02-05-2023", "03-39")

write.invoice_manufacturer(name_manufac, products, amounts, "02-05-2023", "03-39")

'''
#display.admin_pw(1111)

import encrypt

display.admin_mode()
