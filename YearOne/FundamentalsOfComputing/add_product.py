#module adds a new product to dictionary
dict_ = dict()
keys = tuple()


def add_product(name, company, price, amount, cpu, gpu):
    '''
    Function takes six arguments. The name of product, the manufacturing company, its price, the amount recieved,
    its CPU architecture, and its GPU architecture. The data is then parsed into its respective keys in the stock dictionary.
    '''
    data_list = [name, company, price, amount, cpu, gpu]
    data_index = 0
    for key in keys:
        dict_[key].append(data_list[data_index])
        data_index +=1
    del data_list

def ap2(product_details):
    data_index = 0
    for key in keys:
        dict_[key].append(product_details[data_index])
        data_index +=1
    print("Product added!")

def remove_product(product_id):
    '''
    Index value is returned from display
    '''
    for key in keys:
        del dict_[key][product_id]
    print("Product removed!")