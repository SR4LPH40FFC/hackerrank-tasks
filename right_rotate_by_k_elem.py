"""
Title: Right Rotate an array by k elements
Description: An array of elements arr is given. "arr" is of length n.
Right rotate array by k elements. Time complexity O(n) and space complexity O(1)

Sample Input:
arr = [1,2,3,4,5]
n = 5
k = 2
Output: arr = [4,5,1,2,3]
"""

def right_rotate(arr, n, k):

    # incorrect parameters
    # length of array cannot be less than the span from the right
    if(n < k):
        return None

    i = 0
    l = []
    while ((n-1)-k+1+i <= n-1):
        l.append(arr[n-1-k+1+i])
        i+=1

    i = 0
    while(i < (n-1)-k+1):
        l.append(arr[i])
        i+=1

    return l

print right_rotate([1,2,3,4,5], 5, 2)
