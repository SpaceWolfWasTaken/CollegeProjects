#read module
dict_ = dict()
keys = tuple()

def read_file(file_name = "stock.txt") ->  bool:
    '''
    Parameter takes the name of file as an argument.
    Reads a file, converts the data inside and saves it in a list,
    and adds the data in the list to their respective keys in a dictionary
    '''
    with open(".\\Stock\\"+file_name) as stock_file:

        lines = stock_file.readlines()
        for data in lines:
            list_ = data.split(",")
            index_ = 0
            for key in keys:
                if key=="GPU":
                    dict_[key].append(list_[index_].replace("\n",""))
                elif key=="Price":
                    #try block 
                    price_ = int(str(list_[index_].lstrip())[1:]) #removes $ and converts price to integer
                    dict_[key].append(price_)
                elif key=="Amount":
                    #try block
                    dict_[key].append(int(list_[index_].lstrip())) #converts amount to integer
                else:    
                    dict_[key].append(list_[index_])
                index_ +=1
    return True




