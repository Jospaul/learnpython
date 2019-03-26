#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    i = 0
    count = 0
    numberofstickscut = []
    small = fetchSmallThanZero(arr.copy())
    while sum(arr) > 0:
        if i < len(arr):
            if arr[i] > 0:
                arr[i] = arr[i] - small
                count = count + 1
            i = i + 1
        else:
            numberofstickscut.append(count)
            small = fetchSmallThanZero(arr.copy())
            i = 0
            count = 0
    numberofstickscut.append(count)
    return numberofstickscut


def fetchSmallThanZero(arr):
    sorted(arr)
    for i in range(len(arr)):
        if arr[i] > 0:
            return arr[i]


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print('\n'.join(map(str, result)))
    print('\n')

