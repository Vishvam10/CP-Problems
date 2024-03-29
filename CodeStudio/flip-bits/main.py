from os import *
from sys import *
from collections import *
from math import *


def flipBits(arr, n):

    curSum = 0
    maxSum = 0
    ones = 0

    # Make all 0 as 1 and 1 as -1.
    # Also store the number of 1s present initially
    for i in range(n):
        if (arr[i] == 0):
            arr[i] = 1
        else:
            arr[i] = -1
            ones += 1

    # Do Kadane's to get the max sum of subarray
    for i in range(n):
        curSum += arr[i]
        maxSum = max(maxSum, curSum)
        if (curSum < 0):
            curSum = 0

    return maxSum + ones
