def count_inversions(a):
    temp = a[:] # [None for x in range(len(a))]
    return mergesort(a, temp, 0, len(a)-1)

def mergesort(a, temp, leftStart, rightEnd):
    if (leftStart >= rightEnd):
        return 0

    mid = (leftStart + rightEnd) / 2

    inversions = 0
    inversions += mergesort(temp, a, leftStart, mid)
    inversions += mergesort(temp, a, mid+1, rightEnd)

    inversions += mergeHalves(a, temp, leftStart, rightEnd)

    # print a
    return inversions



def mergeHalves(a, temp, leftStart, rightEnd):

    mid = (leftStart + rightEnd) / 2
    sz = rightEnd - leftStart + 1
    leftEnd = mid
    rightStart = mid + 1

    left = leftStart
    right = rightStart

    index = leftStart

    inversions = 0

    while left <= leftEnd or right <= rightEnd:
        if left > leftEnd:
            a[index] = temp[right]
            right += 1
        elif right > rightEnd:
            a[index] = temp[left]
            left += 1
        elif temp[left] <= temp[right]:
            a[index] = temp[left]
            left += 1
        else: # if a[left] > a[right]:
            a[index] = temp[right]
            right += 1
            inversions += mid + 1 - left
        index += 1

    return inversions


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print count_inversions(arr)
