from os import *
from sys import *
from collections import *
from math import *

# Following is the structure of Tree Node:
# Do not update or change the structure 

class TreeNode:

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
def maxHeightDifference(root):

    def ht(node) :
        if(node == None) :
            return 0
        
        left = ht(node.left)
        right = ht(node.right)
        ans = 1 + max(left, right)

        return ans

    
    def solve(node) :
        if(node == None) :
            return 0
        
        lh = ht(node.left)
        rh = ht(node.right)
        diff = abs(rh - lh)

        left = solve(node.left)
        right = solve(node.right)
        ans = max(diff, max(left, right))
        
        return ans
        
    ans = solve(root)

    return ans
