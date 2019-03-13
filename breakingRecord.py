#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highscore = scores[0]
    lowscore = scores[0]
    highcount = 0
    lowcount = 0
    for i in range(1,len(scores)):
        if highscore < scores[i]:
            highscore = scores[i]
            highcount = highcount + 1
        elif lowscore > scores[i]:
            lowscore = scores[i]
            lowcount = lowcount + 1
    return [highcount, lowcount]

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
    print('\n')

