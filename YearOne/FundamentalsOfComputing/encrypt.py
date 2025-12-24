#encrypt module

def thirty_bit_maker(data):
    data = str(data)
    while len(data) < 30:
        data = "0" + data
    return data


def convert_to_bin(data):
    data = int(data)
    data = bin(data)
    return data[2:]

def reverse(data):
    data = str(data)
    data = data[::-1]
    return data


def invert(data):
    data = str(data)
    inverted_data = ""

    for num in data:
        if num == "1":
            inverted_data += "0"
        else:
            inverted_data += "1"    
    return inverted_data

def convert_bin_to_int(data):
    data = int(data, 2)
    return data

def convert_to_oct(data):
    data = oct(data)
    return data[2:]

def convert_oct_to_int(data):
    data = str(data)
    data = int(data, 8)
    return data





def encrypt(number):
    
    '''
    Algorithm:
    Get a number.
    Reverse the bits.
    Invert the bits.
    Reverse the bits.
    Get back a number.
    Convert to oct
    Reverse the oct
    '''
    bin_num = convert_to_bin(number)
    full_bits_num = thirty_bit_maker(bin_num)
    rev_bits = reverse(full_bits_num)
    invert_bits = invert(rev_bits)
    rev_invert = reverse(invert_bits)
    new_num = convert_bin_to_int(rev_invert)
    oct_new_num = convert_to_oct(new_num)

    return oct_new_num

def deencrypt(number):
    '''
    Opposite of encrypt.
    '''
    num = convert_oct_to_int(number)
    bin_num = convert_to_bin(num)
    rev_bits = reverse(bin_num)
    invert_bits = invert(rev_bits)
    rev_invert_bits = reverse(invert_bits)
    full_num = convert_bin_to_int(rev_invert_bits)
    return full_num
