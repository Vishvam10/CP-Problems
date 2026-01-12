from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys


def findPosition(arr, n, playerScore, m):
    ranks, ans = [], []
    ranks.append(arr[0])

    for i in range(1, n, 1):
        if arr[i - 1] != arr[i]:
            ranks.append(arr[i])

    i = len(ranks) - 1

    for score in playerScore:
        while i >= 0 and score >= ranks[i]:
            i -= 1

        ans.append(i + 2)

    return ans
