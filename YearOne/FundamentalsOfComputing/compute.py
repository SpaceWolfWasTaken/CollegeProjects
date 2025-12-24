#compute module

#gets info and make changes to dictionary (amount of products)

dict_ = dict()
keys = tuple() #unneeded. used to make looping easier in main
#make function to calcuate prices

def total_price(price = ()) -> int:
    total = 0
    for num in price:
        total += num
    return total



def check_item(product_id)->bool:
    '''
    Function takes id of the product as argument. If product exists then returns true.
    Else returns false.
    '''
    if product_id > 0 and product_id <= len(dict_["Name"]):
        return True
    return False

def check_buyable(product_id, amount)-> bool:
    '''
    Function takes product id and amount as argument. If argument amount is less than product available, return True.
    Else return false.
    '''
    total_amt = dict_["Amount"][product_id-1]
    if (total_amt - amount) >=0:
        return True
    return False


def inventory_change(client, product_id, amount):
    '''
    Function takes three arguments. client refers to whether it is a customer or manufacturer. product_id is the id of product in table.
    amount is the amount of products to increase/decrease, depending on client.
    '''
    initial_amount = dict_["Amount"][product_id-1]
    newAmount = 0
    if client == "customer":
        newAmount = initial_amount - amount
    if client == "manufacturer" or client == "supplier":
        newAmount = initial_amount + amount
    dict_["Amount"][product_id-1] = newAmount

def remove_product(product_id) -> bool:
    product_id = product_id - 1
    for key in keys:
        del dict_[key][product_id]
    return True
