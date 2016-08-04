#!/usr/bin/python

"""
Objective: Write a function to find all the combinations of three numbers that sum to zero
Sample input: 
[2, 3, 1, -2, -1, 0, 2, -3, 0]
Sample output:
2, -2, 0
1, -1, 0
3, -2, -1
3, 0, -3
3, 0, -3
"""

_input = [2, 3, 1, -2, -1, 0, 2, -3, 0]
_output = []

# divide into negative and positive
negative = []
positive = []

for i in _input:
    if i<0:
        negative.append(i)
    else:
        positive.append(i)

# make a unique list of numbers
negative = sorted(set(negative))
positive = sorted(set(positive))

for p in positive:
    for n in negative:
        if(p+n>0):
            for i in negative:
                if p+n+i > 0:
                    break
                elif p+n+i == 0:
                    _output.append([p,n,i])
        else:
            for i in positive:
                if p+n+i > 0:
                    break
                elif p+n+i == 0:
                    _output.append([p,n,i])

for i in _output:
    print i[0], i[1], i[2]

