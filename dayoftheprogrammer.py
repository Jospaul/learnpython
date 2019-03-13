#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    greg = True
    if year < 1919:
        greg = False
    daysbeforprog = 243
    daysuntil = 0
    if greg:
        if (year % 4) == 0:
            if (year % 400) == 0:
                daysuntil = 256 - (daysbeforprog + 1)
            elif (year % 100) != 0:
                daysuntil = 256 - (daysbeforprog + 1)
            else:
                daysuntil = 256 - daysbeforprog
        else:
            daysuntil = 256 - daysbeforprog
    else:
        if year == 1918:
            daysuntil = 256 - (daysbeforprog - 13)
        elif year % 4 == 0:
            daysuntil = 256 - (daysbeforprog + 1)
        else:
            daysuntil = 256 - daysbeforprog
    return str(daysuntil)+".09."+str(year)

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result + '\n')

