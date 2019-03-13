#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    for i in range(len(s) + 1 - m):
        j = 0
        sumof = 0
        while j < m:
            sumof = sumof + s[i+j]
            j = j + 1
        if sumof == d:
            count = count + 1
    return count

if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')

