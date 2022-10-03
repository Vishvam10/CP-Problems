# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def dfs(root, ans) :
        #     if(root) :
        #         ans.append(root.val)
        #         dfs(root.left, ans)
        #         dfs(root.right, ans)
        # ans = []
        # dfs(root, ans)
        # return ans
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
        
        
        