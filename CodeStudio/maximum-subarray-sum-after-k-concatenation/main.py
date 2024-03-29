from os import *
from sys import *
from collections import *
from math import *


def kadane(arr, n, k):
    curSum = 0
    maxSum = float("-inf")

    for i in range(n*k):
        curSum += arr[i % n]
        maxSum = max(maxSum, curSum)
        if (curSum < 0):
            curSum = 0

    return maxSum


def maxSubSumKConcat(arr, n, k):

    if (k == 1):
        return kadane(arr, n, k)

    s = sum(arr)

    if (s <= 0):
        return kadane(arr, n, 2)
    else:
        maxSum = kadane(arr, n, 2)
        maxSum += (k-2) * s
        return maxSum
