from os import *
from sys import *
from collections import *
from math import *


def subsequences(s):

    n = len(s)
    p = 1 << n
    ans = []

    for i in range(p):
        temp = []
        for j in range(n):
            if ((i >> j) & 1):
                temp.append(s[j])
        ans.append(''.join(temp))

    # Exclude the empty string
    return ans[1:]
