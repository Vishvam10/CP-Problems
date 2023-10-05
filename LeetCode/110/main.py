"""
DIFFICULTY : easy
TAGS : tree, dfs, binary tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_diff(root) :
            if(root is None) :
                return 0

            ls = check_diff(root.left)
            rs = check_diff(root.right)
            if(ls == -1 or rs == -1 or abs(ls - rs) > 1) :
                return -1
            
            return 1 + max(ls, rs)
        
        return check_diff(root) != -1        