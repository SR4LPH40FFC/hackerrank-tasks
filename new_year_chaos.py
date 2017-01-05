#!/bin/python

"""
https://www.hackerrank.com/challenges/new-year-chaos
"""

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(int,raw_input().strip().split(' '))

    # print 'xxx xxx xxx xxx xxx'

    # your code goes here
    i = 0
    ttl_transitions = 0
    while i < n:

        # print i, ':', q

        transitions = 0
        save_i = i
        while (save_i + 1 < n and q[save_i] > q[save_i+1]):
            tmp = q[save_i]
            q[save_i] = q[save_i+1]
            q[save_i+1] = tmp

            transitions += 1
            save_i += 1

            if transitions > 2:
                break

        if transitions == 0:
            i += 1
        elif transitions > 2:
            print 'Too chaotic'
            ttl_transitions = -1
            break
        else:
            if i - 1 >= 0:
                i -= 1
            ttl_transitions += transitions

    if ttl_transitions != -1:
        print ttl_transitions
