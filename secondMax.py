"""
Task: Find the Second Largest Number
URL: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
Description: You are given N numbers. Store them in a list and find the second largest number.
"""

cnt = raw_input()
mylist = map(int, raw_input().split())

max1 = mylist[0]
max2 = None

# O(N log N)
############
# sorted_myset = sorted(myset)
# print sorted_myset[len(sorted_myset)-2]

# O(N)
######
#for i in (myset):
#    if i>max1:
#        max1=i
#
#for i in (myset):
#    if (max2 == None or i>max2) and i<max1:
#        max2=i
#print max2

# O(N) but one cycle walk only
##############################

for i in (mylist):

    if(max2 == None or i > max2) and i < max1:
        max2 = i

    if(i>max1):
        max2=max1
        max1=i

print max2