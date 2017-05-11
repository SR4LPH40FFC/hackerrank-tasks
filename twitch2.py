arr = map(int, raw_input().strip().split())

cur_max = arr[0]
cur_min = arr[0]
cur_min_ind = 0
cur_max_ind = -1

max_diff = -1
diff_max_ind = -1
diff_min_ind = -1

i=0
while i < len(arr):

    if arr[i] < cur_min:
        cur_min_ind = i
        cur_min = arr[i]

        cur_max = arr[i]
        cur_max_ind = -1

    if arr[i] > cur_max:
        cur_max = arr[i]
        cur_max_ind = i
        if cur_max - cur_min > max_diff:
            max_diff = cur_max - cur_min
            diff_max_ind = cur_max_ind
            diff_min_ind = cur_min_ind

    # print "{0} = {1} (arr[{2}]) - {3} (arr[{4}])".format(max_diff, cur_max, cur_max_ind, cur_min, cur_min_ind)
    i+=1

if cur_max - cur_min > max_diff:
    max_diff = cur_max - cur_min
    diff_max_ind = cur_max_ind
    diff_min_ind = cur_min_ind

if max_diff == 0:
    print "-1 [,]"
else:
    print "{0} [{1},{2}]".format(max_diff, diff_min_ind, diff_max_ind)
"""
Sample input:
=============
7 2 3 10 2 4 8 1 10 4 5 3 2 1
4 3 2 1 0
1 2 3 4 5 6
"""