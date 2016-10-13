#!/bin/python

"""
Description: given a pattern and a string, check whether the string matches the
pattern. For example, pattern "aba" and the string is "redbluered" matches
because "a" is translated to "red" and "b" is translated to "blue".

/**
 * Assumptions:
 * 1. pattern contains a set of letters each representing one or 
 * more letters in the input string (no empty string).
 * 
"""

def recursive_search_w_comments(input_string, pattern, ptrn_map):

    global recursive_iteration
    recursive_iteration += 1

    if debug:
        tabs = ""
        for q in xrange(0,recursive_iteration):
            tabs += "\t"
        print tabs,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
        print tabs,'yet another iteration of recursive search function:'
        print tabs,'iiinput:',input_string
        print tabs,'pattern:',pattern
        print tabs,'mapping:',ptrn_map

    # condition to leave the recursion
    if (len(input_string) == 0 and len(pattern) == 0):
        recursive_iteration -= 1
        return True
    elif (len(input_string) == 0 or len(pattern) == 0):
        recursive_iteration -= 1
        return False

    for i in xrange(0, len(input_string)):

        if(debug):
            print tabs,'iterate:',str(i)+": "+str(input_string[0:i+1])

        # if pattern is already set
        if pattern[0] in ptrn_map:
            # if string matches pattern
            if ptrn_map[pattern[0]] == input_string[0:len(ptrn_map[pattern[0]])]:

                if debug:
                    print tabs,"pattern exists: "

                if(recursive_search(input_string[len(ptrn_map[pattern[0]]):], pattern[1:], ptrn_map)):

                    if debug:
                        print tabs,"pattern matches to string"

                    recursive_iteration -= 1
                    return True
                else:

                    if debug:
                        print tabs,"pattern doesn't match to string"

                    continue
            else:
                # string doesn't match the previously found pattern
                if debug:
                    print tabs,"string doesn't match the previously found pattern"

                recursive_iteration -= 1
                return False
        else:

            if debug:
                print tabs,"no pattern, setting and continuing"

            ptrn_map[pattern[0]] = input_string[0:i+1]
            if(recursive_search(input_string[i+1:], pattern[1:], ptrn_map)):
                recursive_iteration -= 1
                return True
            else:
                del ptrn_map[pattern[0]]
                continue

    if debug:
        print tabs+'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

    return False



def recursive_search(input_string, pattern, ptrn_map):

    # condition to leave the recursion
    if (len(input_string) == 0 and len(pattern) == 0):
        return True
    elif (len(input_string) == 0 or len(pattern) == 0):
        return False

    for i in xrange(0, len(input_string)):
        if pattern[0] in ptrn_map: # if pattern is already set
            # if string matches pattern
            if ptrn_map[pattern[0]] == input_string[0:len(ptrn_map[pattern[0]])]:
                if(recursive_search(input_string[len(ptrn_map[pattern[0]]):], pattern[1:], ptrn_map)):
                    return True
                else:
                    continue
            else: # string doesn't match the previously found pattern
                return False
        else:
            ptrn_map[pattern[0]] = input_string[0:i+1]
            if(recursive_search(input_string[i+1:], pattern[1:], ptrn_map)):
                return True
            else:
                del ptrn_map[pattern[0]]
                continue
    return False



debug = 0
recursive_iteration = -1

tests = [
         ["redbluebluered", "abba"],
         ["redblueblueredq", "abba"],
         ["dddddddddd", "abba"],
         ["abba", "abba"],
         ["dogcatcatcat", "abba"]
        ]

for test in tests:
    print test[0], test[1], ': ',
    print recursive_search(test[0], test[1], {})



""" The Algorithm:
a:r
a:r, b:e
-- bad! ptrn_map['b'] != d
a:r, b:ed
-- bad! ptrn_map['b'] != bl
a:r, b:edb
-- bad! ptrn_map['b'] != lue
...
a:r, b:edbluebluered
-- bad! ptrn_map['b'] != ''
-- string empty!
===
a:re
a:re, b:d
-- bad! ptrn_map['b'] != b
a:re, b:db
-- bad! ptrn_map['b'] != lu
...
a:re, b:dbluebluered
-- bad! ptrn_map['b'] != ''
-- string empty!
===
a:red
a:red, b:b
-- bad! ptrn_map['b'] != l
a:red, b:bl
-- bad! ptrn_map['b'] != ue
a:red, b:blu
-- bad! ptrn_map['b'] != ebl
a:red, b:blue
-- success!!!
a:red, b:blue, b:blue
a:red, b:blue, b:blue, a:red

TODO: think of a condition to exit recursion at the end of the word!
"""



"""
def red_blue_blue_red( pattern, input_str ):

    ptrn = []
    cnt_ptrn_ltr = 1

    ptrn_arr = parse_pattern(pattern)
    current_start = 0

    for item in ptrn_arr:

        sub_str = input_str[current_start:]

        for word in pattern_contains_n_items_at_the_beginning(sub_str, item['count']):
            
        
    current_start = len(item['var']) * item['count']

    return True


def parse_pattern( input_string ):

    cnt = 1
    prev = -999
    ptrn = []

    for curr in input_string:

        if (prev == curr):
            cnt += 1
        else:
            if prev != -999:
                ptrn.append({'var': prev, 'count': cnt})
            cnt = 1

        prev = curr

    if prev != -999:
        ptrn.append({'var': prev, 'count': cnt})

    return ptrn

def pattern_contains_n_items_at_the_beginning(input_str, count):

    word = ""
    first_ltr = input_str[0]
    ret = []

    iter = 0

    while 1:

        i = 0
        found = 0
    
        for ltr in input_str:
    
            if first_ltr == ltr and i > 0:
                if found >= iter:
                    break
                else:
                    found += 1
            else:
                word += str(ltr)

            i += 1

        if found < iter:
            return ret
    
        for cnt in xrange(0, count):
            i = 0
            for ltr in word:
                # print str(input_str[len(word)*cnt + i]) + ' =? ' + str(ltr)
                if str(input_str[len(word)*cnt + i]) != str(ltr):
                    return ret
                i += 1

        ret.append(word)

    return ret


# for i in pattern_contains_n_items_at_the_beginning("ddddddabc", 3):
#     print i
#     print "xxxxxxxxxx"


"""