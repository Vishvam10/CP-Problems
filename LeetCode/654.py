# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, arr: List[int]) -> Optional[TreeNode]:
        if(not arr) :
            return
        
        max_val = max(arr)
        max_ind = arr.index(max_val)
        
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(arr[:max_ind])
        root.right = self.constructMaximumBinaryTree(arr[max_ind+1:])
        
        return root