"""
Title: Nested Lists
Description: Given the names and grades for each student in a Physics class of  
students, store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.
Note: If there are multiple students with the same grade, order their names 
alphabetically and print each name on a new line.
"""

import sys

N = int(raw_input())
 
first_names = []
second_names = []
  
first = second = sys.maxint
 
for i in range(N):
    name = str(raw_input())
    grade = float(raw_input())
 
    # If current element is smaller than first then
    # update both first and second
    if grade < first:
        second = first
        first = grade
 
        second_names = first_names
        first_names = [name]
 
    # If grade is in between first and second then
    # update second
    elif (grade == first):
        first_names.append(name)
 
    elif (grade < second):
        second = grade
        second_names = [name]

    elif (grade == second):
        second_names.append(name)
 
 
# print '--- --- --- --- ---'
print "\n".join(sorted(second_names))


