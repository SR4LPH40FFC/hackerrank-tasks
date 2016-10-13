"""
Task: Implement List.reverse()
"""

def reverse(lst):
    for i in xrange(int(len(lst)/2)):
        tmp = lst[i]
        lst[i] = lst[len(lst)-1-i]
        lst[len(lst)-1-i] = tmp

    return lst

l = ['q','w','e','a','s','d','f']
print l
print reverse(l)
