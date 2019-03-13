#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    ms = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    rs = ms[:]
    sumarr = []
    bool = True
    while True:
        sumperrow = 0
        for i,j in zip(s,rs):
            for k in range(len(i)):
                sumperrow = sumperrow + abs(i[k]-j[k])
        sumarr.append(sumperrow)
        rs = rotateMagicSquare(rs, bool)
        bool = not bool
        if rs == ms:
            break
    return min(sumarr)


def rotateMagicSquare(news, bool):
    if bool:
        transp = news[::-1]
        return transp
    else:
        transp = [[row[i] for row in news] for i in range(3)]
        return transp


if __name__ == '__main__':
    l = []
    s = l

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(str(result) + '\n')


