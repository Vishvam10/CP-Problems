"""
DIFFICULTY : medium
TAGS : tree, dfs, bst, binary tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # IDEA : The inorder traversal (LNR) of a BST gives
    #        a sorted array in ascending order
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def helper(node):
            if (not node):
                return []
            return helper(node.left) + [node.val] + helper(node.right)

        return helper(root)[k - 1]
