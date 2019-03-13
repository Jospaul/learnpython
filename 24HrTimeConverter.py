#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    time = s.split(":")
    timeinday = time[2][2:]
    if timeinday == 'PM':
        if int(time[0]) < 12:
            time[0] = str(int(time[0]) + 12)
    else:
        if int(time[0]) > 11:
            time[0] = '00'
    time[2] = time[2][:2]
    hr24time=time[0] + ':' + time[1] + ':' + time[2]

    return hr24time
if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)