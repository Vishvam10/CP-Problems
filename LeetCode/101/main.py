# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(left, right):
            if (left is None and right is None):
                return True
            if (left is None or right is None):
                return False

            if (left.val == right.val):
                inner_pair = isMirror(left.right, right.left)
                outer_pair = isMirror(left.left, right.right)
                return inner_pair and outer_pair
            else:
                return False

        if (root is None):
            return True
        else:
            return isMirror(root.left, root.right)
