"""
Title: map and lambda functions
Description: Let's learn some new Python concepts! You have to generate a list 
of the first  fibonacci numbers,  being the first number. Then, apply the map 
function and a lambda expression to cube each fibonacci number and print the list.
"""

def fib(N):
    if N == 0:
        return []
    elif N == 1:
        return [0]

    l = [0,1]
    for i in range(2,N):
        l.append(l[i-2]+l[i-1])
        i+=1

    return map(lambda i: i**3, l)

N = int(raw_input().strip())
print fib(N)