"""
DIFFICULTY : medium
TAGS : tree, binary tree, dfs
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def helper(node, val) :
            if(not node) :
                return 0
            val = val*10 + node.val
            if(not node.left and not node.right) :
                return val 
            return helper(node.left, val) + helper(node.right, val)
        
        return helper(root, 0)