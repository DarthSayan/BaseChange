#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
# ----------------------------------------------------------------------------
"""
CambioDeBase: (BaseChange) Is a tool to calculate the numerical representation of a number given by the user
in different representation bases: binary, decimal, octal and hexadecimal.
"""
__author__ = "DarthSayan"
__copyright__ = "Copyright 2024, ATG"
__credits__ = ["Gonzalez Neila, Samuel"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Gonzalez Neila, Samuel"
__email__ = ""
__status__ = "Production"

# date (YYYY-MM-DD): 2023-02-04

from baseSelector import *


if __name__ == '__main__':
    # Show options menu:
    show_options()

    # Ask for tha base of the number to convert
    option = input('Select one of the above options. ')
    option_selected(str(option))


