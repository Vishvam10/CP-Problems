"""
DIFFICULTY : medium
TAGS : tree, dfs, binary tree, binary search tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Create a helper function for recursion
    
    # Use 2 global variables low and high to keep track of
    # the minimum and maximum value upto that node.  
    
    # The low and high update is simple : 
    # FOR LEFT SUBTREE : low = low ( no change ), high = root.val
    # FOR RIGHT SUBTREE : low = root.val, high = high ( no change )
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root, low, high) :
            if not root :
                return True
            elif not low < root.val < high :
                return False
            else :
                return traverse(root.left, low, root.val) and traverse(root.right, root.val, high)
        return traverse(root, low=float("-inf"), high=float("inf"))
            