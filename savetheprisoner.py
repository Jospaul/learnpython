#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    pris = s + m - 1
    finalpris = pris%n
    if finalpris == 0:
        return n
    else:
        return finalpris


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(str(result) + '\n')

