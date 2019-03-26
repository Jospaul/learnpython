#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    count = 0
    i = a
    while i <= b:
        if math.sqrt(i).is_integer():
            count = count + 1
            i = i + int(abs(i - ((math.sqrt(i) + 1)*(math.sqrt(i) + 1)) ))
        else:
            i = i + 1
    return count
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        print(str(result) + '\n')
