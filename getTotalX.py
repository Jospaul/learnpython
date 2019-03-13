#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#


def lcm(a, b):
    lcm = (a*b)/gcd(a, b)
    return lcm

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcmarr(a):
    lcmval = a[0]
    for i in range(1,len(a)):
        lcmval = lcm(lcmval,a[i])
    return lcmval

def gcdarr(b):
    gcdval = b[0]
    for i in range(1,len(b)):
        gcdval = gcd(gcdval,b[i])
    return gcdval

def getTotalX(a, b):
    count = 0
    l = lcmarr(a)
    g = gcdarr(b)
    i=l
    j=2
    while i<=g:
       if g%i == 0:
           count = count + 1
       i = j*l
       j = j + 1
    return count


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    print(str(total) + '\n')

