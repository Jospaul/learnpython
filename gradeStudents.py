#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    nearmulfive = 0
    diffwithmulfive = 0
    for i in range(len(grades)):
        if grades[i] > 37:
            nearmulfive = (5 - (grades[i] % 5)) + grades[i]
            diffwithmulfive = nearmulfive - grades[i]
            if diffwithmulfive < 3:
                grades[i] = nearmulfive

    return grades
if __name__ == '__main__':

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
    print('\n')
