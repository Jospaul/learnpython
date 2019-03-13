#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar = sorted(ar)
    pairs = {}
    i = 0
    while i < len(ar):
        count = 1
        for j in range(i+1, len(ar)):
            if ar[j] == ar[i]:
                count = count + 1
            else:
                break
        pairs[ar[i]] = count
        i = i + count

    count = 0
    for keys in pairs:
        if pairs[keys] % 2 == 0:
            count = count + pairs[keys]/2
        else:
            if pairs[keys] > 2:
                count = count + int(pairs[keys]/2)
    return int(count)

if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')

