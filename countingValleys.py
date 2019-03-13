#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    steps = 0
    count = 0
    valley = False
    for i in range(len(s)):
        if s[i] == 'D':
            steps = steps + 1
            if steps > 0:
                valley = True
        elif (s[i] == 'U'):
            steps = steps - 1
            if steps < 0:
                valley = False
        if (steps == 0) & valley:
            count = count + 1

    return count
if __name__ == '__main__':
    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(str(result) + '\n')
