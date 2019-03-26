#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if k > abs(len(s) + len(t)) and t in s:
        return "Yes"
    elif k > abs(len(t)-len(s)):
        if t == s:
            j = k - len(t)
            for i in range(j):
                s = delete(s)
            k = k - j
        elif "".join(reversed(t)) == s:
            j = k - len(s)
            s = ''
            k = k - j


        while k > 0:
            if t in s:
                s = delete(s)
            elif s in t:
                s = append(s, t, len(s))
            else:
                s = delete(s)
            k = k - 1

    if s == t:
        return "Yes"
    else:
        return "No"

def delete(s):
    return s[:-1]

def append(s,t,i):
    s = s + t[i]
    return s



if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    print(result + '\n')
