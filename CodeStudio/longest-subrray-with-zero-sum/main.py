from math import *
from collections import *
from sys import *
from os import *


def LongestSubsetWithZeroSum(arr):

    mp = defaultdict(int)
    pref, ans = 0, 0
    for (i, x) in enumerate(arr):
        pref += x
        if (pref in mp):
            ans = max(ans, i-mp[pref])
        else:
            if (pref == 0):
                ans = max(ans, i+1)
            else:
                mp[pref] = i

    return ans
