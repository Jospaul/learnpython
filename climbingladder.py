#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    rank = []
    currank = 1
    prevrank = 0
    for i in range(len(alice)):
        j = i
        while j < len(scores):
            if alice[i] >= scores[j]:
                if j == 0:
                    currank = 1
                elif j > 0:
                    if scores[j] < scores[j-1]:
                        currank = currank - 1
            elif alice[i] == scores[j]:
                currank = prevrank
            elif alice[i] < scores[j]:
                if j > 0:
                    if scores[j] < scores[j-1]:
                        currank = currank + 1
                else:
                    currank = currank + 1
            prevrank = currank
            j = j+1
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

