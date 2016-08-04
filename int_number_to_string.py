#!/usr/bin/python

"""
Task: Convert number to string
URL: no link
Description: Convert given number to a text representation of the same number
"""

import math

digits = (
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
)

tens = (
    'zero',
    'ten',
    'twenty',
    'thirty',
    'fourty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
)

powers = {
    2:  'hundred',  # 100                   # 10^2
    3:  'thousand', # 1000                  # 10^3
    6:  'million',  # 1.000.000             # 10^6
    9:  'billion',  # 1.000.000.000         # 10^9
    12: 'trillion'  # 1.000.000.000.000     # 10^12
}

input_integers = (12, 4345, 7654567643, 98234)

# qwe = int(45 / 10)
# print qwe
# exit()

for i in (input_integers):
    print str(i)+": ",
    for p in (12,9,6,3,2,1): # todo: sort {$b <=> $a} keys powers
        res = int(i / pow(10,p))
#         print "DEBUG: "+str(i)+" / "+str(pow(10,p))+" = "+str(res)
        print_s = ""
        if res > 1: print_s = "s"
        if (res > 0):
            if p == 1:
                if i>19:
                    print " "+str(tens[res]),
                    i = i % 10
                if i>0:
                    print " "+str(digits[i]),
            else:
                print " "+str(res) +" "+ str(powers[p]) + print_s,

        i = i % pow(10,p)
    print






