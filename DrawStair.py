#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    count = n
    arr = []

    for i in range(n):
        small = []
        for j in range(count):
            small.append("#")
        arr.append(small)
        count = count - 1
    for i in range(n):
        top = arr.pop()
        toplen = len(top)
        if toplen < n:
            for i in range(n - toplen):
                top.append(" ")
            top.reverse()
        stri = ''
        for j in range(len(top)):
            stri = stri + top[j]
        print(stri)


if __name__ == '__main__':
    n = int(input())

    staircase(n)