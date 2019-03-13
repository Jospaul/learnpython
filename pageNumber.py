#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    fromBeg = 0
    fromEnd = 0
    if n == 0:
        return 0
    else:
        if p%2 == 0:
            fromBeg = int(p / 2)
            fromEnd = int((n-p)/2)
        else:
            fromBeg = int((p-1)/2)
            if n%2 == 0:
                fromEnd = int((n-p)/2) + 1
            else:
                fromEnd = int((n-p)/2)

    return min(fromBeg,fromEnd)



if __name__ == '__main__':

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(str(result) + '\n')
