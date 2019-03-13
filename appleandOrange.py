#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applecount = 0
    orangecount = 0
    distcalc = 0
    for i in range(len(apples)):
        distcalc = a + apples[i]
        if distcalc in range(s,t+1):
            applecount = applecount + 1
    for i in range(len(oranges)):
        distcalc = b + oranges[i]
        if distcalc in range(s,t+1):
            orangecount = orangecount + 1

    print(applecount)
    print(orangecount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)