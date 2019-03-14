#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    rank = []
    currank = len(set(scores)) + 1
    j = len(scores) - 1
    limit = len(scores) - 1
    for i in range(len(alice)):
        count = 0
        while alice[i] >= scores[j]:
            if (j >= 0) & (j < (len(scores) - 1)):
                if (scores[j] <= scores[j-1]) & (scores[j] > scores[j+1]):
                    count = count + 1
            elif j >= 0:
                if scores[j] < scores[j - 1]:
                    count = count + 1
            else:
                break
            j = j - 1

        limit = limit - count
        j = limit
        if count > 0:
            currank = currank - count
        rank.append(currank)
    return rank

if __name__ == '__main__':
    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print('\n'.join(map(str, result)))
    print('\n')

