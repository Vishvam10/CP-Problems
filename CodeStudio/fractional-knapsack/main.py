from os import *
from sys import *
from collections import *
from math import *


def maximumValue(items, n, w):
    # Write your code here.
    # ITEMS contains [weight, value] pairs.
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    ans = 0
    for x in items:
        if x[0] < w:
            ans += x[1]
            w -= x[0]
        else:
            ans += (x[1] / x[0]) * w
            w = 0
            break
    return ans
