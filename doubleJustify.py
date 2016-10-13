#!/bin/python

"""
Task: Double Justify
URL: no link
Description: double justify given string 
"""

def doubleJustify(iStr, icnt):

    # check input
    # ...
    
    spacesToAdd = icnt - len(iStr)
    if spacesToAdd < 0:
        return iStr

    iStrWords = iStr.strip().split()

    ratio = int(spacesToAdd / (len(iStrWords)-1))
    leftOff = spacesToAdd - ratio * (len(iStrWords)-1)

    spaceStr = "." # 1 initial and N additional
    for i in xrange(ratio):
        spaceStr += "." 

    ret = ""

    for w in (iStrWords):
        ret += w+spaceStr
        if leftOff > 0:
            ret += "."
            leftOff -= 1

    ret = ret.strip(".")

    return ret

print doubleJustify("I am OK", 20)