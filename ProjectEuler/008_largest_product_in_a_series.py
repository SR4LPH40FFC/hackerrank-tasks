"""
Task: Project Euler #8: Largest product in a series
URL: https://www.hackerrank.com/contests/projecteuler/challenges/euler008
Description: Find the greatest product of K consecutive digits in the N digit number.
"""

t = int(raw_input().strip())

for a0 in xrange(t):

    # get input
    n,k = map(int, raw_input().strip().split(' '))
    num = raw_input().strip()

    # init vars
    str_num = str(num)
    idx = 0
    max_mtlply = 0
    max_num = None

    # loop through digits in a number
    for ch in str_num:
        if idx > len(str_num) - k:
            break
        # get number on current index
        cur_num = str_num[idx:idx+k]

        # multiply digits
        cur_mltply = reduce(lambda x,y: int(x)*int(y), cur_num)

        # identify max
        if cur_mltply > max_mtlply:
            max_mtlply = cur_mltply
            max_num = cur_num

        idx += 1

    print max_mtlply