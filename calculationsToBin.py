from featuredTools import reverse_string

"""
    Function to switch a number from base 10 to base 2
"""
def decimal_to_binary(num, bin_num):
    bin_string = ""
    if num <= 1:
        return str(num)
    else:
        result = num
        while result > 1:
            bin_string = bin_string + str(result%2)
            result=int(result/2)
        else:
            bin_string = bin_string + str(result)

    return reverse_string(bin_string)

"""
    Function to switch a number from base 8 to base 2
"""
def octal_to_binary(num):
    octal_binaries = {
        '0':'000',
        '1':'001',
        '2':'010',
        '3':'011',
        '4':'100',
        '5':'101',
        '6':'110',
        '7':'111'
    }
    binary_string = ""
    for i in str(num):
       binary_string = binary_string + octal_binaries.get(i)

    return binary_string


"""
    Function to switch a number from base 16 to base 2
"""
def hexa_to_binary(num):
    hexa_binaries = {
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111'
    }
    binary_string = ""
    for i in str(num).upper():
       binary_string = binary_string + hexa_binaries.get(i)

    return binary_string


result=hexa_to_binary("a")
print(result)
result=octal_to_binary(255)
print(result)
result=decimal_to_binary(10,"")
print(result)