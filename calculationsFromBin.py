"""
    Function to switch a number from base 2 to base 8
"""

def binary_to_octal(num):
    binaries_octal = {
        '000':'0',
        '001':'1',
        '010':'2',
        '011':'3',
        '100':'4',
        '101':'5',
        '110':'6',
        '111':'7'
    }

    if len(str(num))%3 == 0:
        bin_string = ""
    elif len(str(num))%3 == 1:
        bin_string = "00"
    elif len(str(num))%3 == 2:
        bin_string = "0"

    bin_string = bin_string + num
    octal_string = ""

    i=0
    while i < len(bin_string):
        dict_key = bin_string[i] + bin_string[i+1] + bin_string[i+2]
        octal_string = octal_string + binaries_octal.get(dict_key)
        i += 3
    return octal_string


"""
    Function to switch a number from base 2 to base 8
"""

def binary_to_decimal(num):
    bin_string = str(num)
    scale = len(bin_string)-1
    num_dec = 0
    for i in range (len(bin_string)):
        if bin_string[i] == "1":
            num_dec = num_dec + (pow(2,scale))
        scale -=1
    return num_dec


"""
    Function to switch a number from base 2 to base 16
"""

def binary_to_hexa(num):
    binaries_hexa = {
        '0000':'0',
        '0001':'1',
        '0010':'2',
        '0011':'3',
        '0100':'4',
        '0101':'5',
        '0110':'6',
        '0111':'7',
        '1000':'8',
        '1001':'9',
        '1010':'A',
        '1011':'B',
        '1100':'C',
        '1101':'D',
        '1110':'E',
        '1111':'F'
    }

    if len(str(num))%4 == 0:
        bin_string = ""
    elif len(str(num))%4 == 1:
        bin_string = "000"
    elif len(str(num))%4 == 2:
        bin_string = "00"
    elif len(str(num))%4 == 3:
        bin_string = "0"

    bin_string = bin_string + str(num)
    hexa_string = ""

    i=0
    while i < len(bin_string):
        dict_key = bin_string[i] + bin_string[i+1] + bin_string[i+2] + bin_string[i+3]
        hexa_string = hexa_string + binaries_hexa.get(dict_key)
        i += 4
    return hexa_string