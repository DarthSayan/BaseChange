from resultOfCalculations import *

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
                num = int(input(f'Enter the decimal you want to convert: '))
                conversions_from_dec(num)
            elif selection == "2":
                num = int(input(f'Enter the binary you want to convert: '), 2)
                conversions_from_bin(num)
            elif selection == "3":
                num = int(input(f'Enter the octal you want to convert: '), 8)
                conversions_from_oct(num)
            elif selection == "4":
                num = int(input(f'Enter the hexadecimal you want to convert: '), 16)
                conversions_from_hex(num)
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
