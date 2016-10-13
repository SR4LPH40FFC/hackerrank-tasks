"""
Title: Finding the percentage
Description: You have a record of N students. Each record contains the student's 
name, and their percent marks in Maths, Physics and Chemistry. The marks can be 
floating values. The user enters some integer N followed by the names and marks 
for N students. You are required to save the record in a dictionary data type. 
The user then enters a student's name. Output the average percentage marks 
obtained by that student, correct to two decimal places.
"""

N = int(raw_input())
students = {}

for i in range(N):
    tmp = raw_input().strip().split()
    students[tmp[0]] = map(float, tmp[1:])

name = raw_input()

summ = 0
cnt = 0

for i in students[name]:
    summ += i
    cnt += 1

if cnt > 0:
    print "{:.2f}".format(summ/cnt)
else:
    print None