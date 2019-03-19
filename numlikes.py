#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    numlikes = 0
    shares = 5
    for i in range(n):
        numlikes = numlikes + int(shares/2)
        shares = numlikes * 3
    return numlikes

if __name__ == '__main__':

    n = int(input())

    result = viralAdvertising(n)

    print(str(result) + '\n')

