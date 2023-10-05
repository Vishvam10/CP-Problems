from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit

setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

    curSum = 0

    # Actually, it should be float("-inf") but the output
    # expects 0 if all the elements are negative
    maxSum = 0  

    for i in range(n) :
        curSum += arr[i]
        maxSum = max(maxSum, curSum)
        if(curSum < 0) :
            curSum = 0
    
    return maxSum
