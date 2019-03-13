#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    totsum = 0
    finalval = 0
    for i in range(len(bill)):
        totsum = totsum + bill[i]
    anncon = (totsum - bill[k])/2

    finalval = b - anncon
    if finalval == 0:
        print("Bon Appetit")
    else:
        print(str(int(finalval)))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)