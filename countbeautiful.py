#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    for a in range(i,j+1):
        if abs(reverseNumber(int(a)) - a) % k == 0:
            count = count + 1
    return count

def reverseNumber(num):
    reversenum = 0
    while(num!=0):
        reversenum = reversenum * 10
        reversenum = reversenum + int(num%10)
        num = int(num / 10)
    return reversenum

if __name__ == '__main__':

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(str(result) + '\n')