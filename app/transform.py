# -*- coding: utf-8 _*_
#Convert-data-format

#########################################################
####                                                 ####
#### Antonio Galvan  agalvan@astro.unam.mx           ####
#### Module to transfor a string into a table data   ####
####                                                 ####
#########################################################


def __checkNumber(row_to_check):
    try:
        if float(row_to_check[0]) and float(row_to_check[1]):
            return True
    except ValueError:
        return False


def single_points(data):

    '''
    Function to give format of a pair of points,
    the output are of the form
    x, y, xerror_low, xerror_high, yerror_high, yerror_low
    '''

    data_list = data.split("\n")

    for i in data_list:
        for j in  i.split("\n"):
            tmp = j.split("\t")
            if __checkNumber(tmp):
                print tmp[0], tmp[1]
            else:
                pass
