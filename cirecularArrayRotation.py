#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):

    if k >= len(a):
        f = k % len(a)
        if f > int(len(a)/2):
            a = a[(f + 1):] + a[:(f + 1)]
        else:
            a = a[(len(a) - f):] + a[:(len(a) - f)]
    else:
        if k > int(len(a)/2):
            a = a[len(a)%k:] + a[:len(a)%k]
        else:
            a = a[abs(len(a) - k):] + a[:abs(len(a) - k)]
    return [a[queries[j]] for j in range(len(queries))]

if __name__ == '__main__':
    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print('\n'.join(map(str, result)))
    print('\n')

