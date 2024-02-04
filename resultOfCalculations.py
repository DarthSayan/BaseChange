from calculationsFromBin import *
from calculationsToBin import *

def conversions_from_bin(num):
    print(f'Base 2 number {num} has the following values in the different bases of representation:')
    print(f'    Base-8:     {binary_to_octal(num)}')
    print(f'    Base-10:     {binary_to_decimal(num)}')
    print(f'    Base-16:    {binary_to_hexa(num)}')


def conversions_from_oct(num):
    print(f'Base 8 number {num} has the following values in the different bases of representation:')
    print(f'    Base-2:     {octal_to_binary(num)}')
    print(f'    Base-10:     {binary_to_decimal(octal_to_binary(num))}')
    print(f'    Base-16:    {binary_to_hexa(octal_to_binary(num))}')


def conversions_from_dec(num):
    print(f'Base 10 number {num} has the following values in the different bases of representation:')
    print(f'    Base-2:     {decimal_to_binary(num, "")}')
    print(f'    Base-8:     {binary_to_octal(decimal_to_binary(num, ""))}')
    print(f'    Base-16:    {binary_to_hexa(decimal_to_binary(num, ""))}')


def conversions_from_hex(num):
    print(f'Base 16 number {num} has the following values in the different bases of representation:')
    print(f'    Base-2:     {hexa_to_binary(num)}')
    print(f'    Base-8:     {binary_to_octal(hexa_to_binary(num, ""))}')
    print(f'    Base-10:    {binary_to_decimal(hexa_to_binary(num, ""))}')
