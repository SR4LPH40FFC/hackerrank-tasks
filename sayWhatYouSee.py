"""
Description: given a list of strings (each string consists of 1 or more numbers)
print a list of strings (each string will consist of 2 or more numbers) using the 
idea from the following example:

input: 21113
processing step 1: the given number consists of one digit 2, 3 digits of 1 and 1 digit 3
processing step 2: one digit 2 is translated to 12, 3 digits of 1 translated to 31, 1 digit 3 translated to 13
processing step 3: result is 123113
"""

def  say_what_you_see( input_strings ):

    ret = []

    for number in (input_strings):

        cnt = 1

        curr_ret = ""
        prev = -999

        for curr in number:

            if (prev == curr):
                cnt += 1
            else:
                if prev != -999:
                    curr_ret += str(cnt) + str(prev)
                cnt = 1

            prev = curr

        if prev != -999:
            curr_ret += str(cnt) + str(prev)

        ret.append(curr_ret)

    return ret


print say_what_you_see(["1", "12", "21", "21114", "11111111111", "000211112221"])