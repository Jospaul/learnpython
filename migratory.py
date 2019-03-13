#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr = sorted(arr)
    migbirds = 0
    val = 0
    i = 0
    while i < len(arr):
        count = 1
        for j in range(i+1,len(arr)):
            if arr[j] == arr[i]:
                count = count + 1
            else:
                break
        if val < count:
            val = count
            migbirds = arr[i]
        i = i + count

    return migbirds

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')
