from resultOfCalculations import *
from featuredTools import check_if_binary
from featuredTools import check_if_octal
from featuredTools import check_if_hex


def show_options():
    print(f'What kind of number do you want to convert?')
    print(f'1 --> Dec')
    print(f'2 --> Bin')
    print(f'3 --> Oct')
    print(f'4 --> Hex')

def number_to_convert(selection, retries):
    if retries < 3:
        try:
            if selection == "1":
                num_d = str(int(input(f'Enter the decimal you want to convert: ')))
                conversions_from_dec(num_d)
            elif selection == "2":
                num_b = str(input(f'Enter the binary you want to convert: '))
                attempts = 0
                while not check_if_binary(num_b):
                    if attempts < 3:
                       number_to_convert(2, retries)
                       attempts += 1
                       num_b = str(input(f'Enter the binary you want to convert: '))
                    else:
                        print(f'Something went wrong. Aborting program')
                        retries = 3
                        break
                conversions_from_bin(num_b)
            elif selection == "3":
                num_o = str(input(f'Enter the octal you want to convert: '))
                attempts = 0
                while not check_if_octal(num_o):
                    if attempts < 3:
                        number_to_convert(3, retries)
                        attempts += 1
                        num_o = str(input(f'Enter the octal you want to convert: '))
                    else:
                        print(f'Something went wrong. Aborting program')
                        retries = 3
                        break
                conversions_from_oct(num_o)
            elif selection == "4":
                num_h = str(input(f'Enter the hexadecimal you want to convert: '))
                attempts = 0
                while not check_if_hex(num_h):
                    if attempts < 3:
                        number_to_convert(4, retries)
                        attempts += 1
                        num_h = str(input(f'Enter the hexadecimal you want to convert: '))
                    else:
                        print(f'Something went wrong. Aborting program')
                        retries = 3
                        break
                conversions_from_hex(num_h)
        except Exception as excp:
            print(f'Something went wrong. Error catched: {excp}')
            retries+=1
            number_to_convert(selection, retries)
    else:
        print(f'Something went wrong. Aborting program')


def option_selected(option):
    flag = 0
    attempts = 1
    retries = 3
    while flag == 0:
        try:
            if attempts < 3 and option not in "1,2,3,4":
                attempts += 1
                print(f'Please, select a valid value.')
                option = str(input('Select one of the above options. '))
            elif attempts>= 3 and option not in "1,2,3,4":
                print(f'Something seems to be wrong. It is your #{attempts} attempt')
                print(f'You have {retries} tries left to select a correct option')
                show_options()
                option = str(input('Select one of the above options. '))
                retries -= 1
                if retries == -1:
                    flag = 2
            else:
                flag = 1
        except Exception as excp:
            flag = 0
            print(f'Something went wrong. Error catched: {excp}')

    if flag == 2:
        print(f'Something went wrong. Aborting program')
    elif flag == 1:
        number_to_convert(option, 0)
