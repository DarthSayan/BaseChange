"""
# Function to reorder a string of characters in reverse order
# (from the end to the beginning)
# by reversing the order of the characters.
"""
def reverse_string(chain):
    reversed_chain = ""
    pointer = len(chain)
    while pointer > 0:
        reversed_chain = reversed_chain + chain[pointer-1]
        pointer -= 1
    else:
        return reversed_chain

"""
# Function to check if a string given by the user
# can be a binary number,
# i.e. only consists of 1s and 0s.
"""
def check_if_binary(num):
    num = str(num)
    flag = True
    for i in num:
        if i not in "0,1":
            flag = False
            break
    return flag

"""
# Function to check if a string given by the user
# can be an octal number,
# i.e. only consists of characters from 0 to 7.
"""
def check_if_octal(num):
    num = str(num)
    flag = True
    for i in num:
        if i not in "0,1,2,3,4,5,6,7":
            flag = False
            break
    return flag

"""
# Function to check if a string given by the user
# can be a hexadecimal number,
# i.e. only consists of characters from 0 to 7.
"""
def check_if_hex(num):
    num = str(num)
    flag = True
    for i in num:
        if i not in "0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,a,b,c,d,e,f":
            flag = False
            break
    return flag