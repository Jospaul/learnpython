#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    global length
    finallist = []
    for i in range(len(a)):
        intermed = []
        for j in range(len(a)):
            if abs(a[j]-a[i]) <= 1:
                intermed.append(a[j])
        maxval = max(intermed)
        length = len(intermed)
        k=0
        while k < length:
            if maxval-intermed[k] > 1:
                intermed.pop(k)
                length = length - 1
                k = k - 1
            k = k+1
            length = len(intermed)

        if len(intermed) > 1:
            finallist.append(intermed)
    finall = [list(x) for x in set(tuple(x) for x in finallist)]
    lengths = [len(x) for x in finall]
    return max(lengths)
if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')
