"""
Task: one away
Description: you have 3 operations on strings: insert, replace, remove
Given 2 strings, identify if one can be transformed into another with a single 
transformation.
"""


def one_away(str1, str2):
    i=0

    if str1 == str2:
        return True

    if(
       len(str1) - len(str2) > 1 or
       len(str2) - len(str1) > 1
    ):
        return False

    for i in xrange(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            if (
                str1[i+1:] == str2[i:] or   # check insert
                str1[i+1:] == str2[i+1:] or # check replace
                str1[i:]   == str2[i+1:]    # check remove
            ):
                return True
            else:
                return False
        i += 1
    # string match
    return True
    

print one_away("abba", "abaa")
