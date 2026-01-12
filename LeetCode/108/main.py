"""
DIFFICULTY : easy
TAGS : array, tree, bst, divide and conquer, binary tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, arr, left, right):
        mid = left + (right - left) // 2
        if left > right:
            return
        root = TreeNode(arr[mid])
        root.left = self.helper(arr, left, mid - 1)
        root.right = self.helper(arr, mid + 1, right)
        return root

    def sortedArrayToBST(self, arr: List[int]) -> Optional[TreeNode]:
        return self.helper(arr, 0, len(arr) - 1)
