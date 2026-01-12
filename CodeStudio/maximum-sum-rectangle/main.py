from os import *
from sys import *
from collections import *
from math import *


def kadane(arr, n):
    curSum = 0
    maxSum = float("-inf")

    for i in range(n):
        curSum += arr[i]
        maxSum = max(maxSum, curSum)

        if curSum < 0:
            curSum = 0

    return maxSum


def maxSumRectangle(arr, n, m):
    curSum = 0
    maxSum = float("-inf")
    temp = []

    for i in range(m):
        temp = [0 for _ in range(n)]
        for j in range(i, m):
            for x in range(n):
                temp[x] += arr[x][j]

            curSum = kadane(temp, n)
            maxSum = max(maxSum, curSum)

    return maxSum
