# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def helper(node, acc, res) :
            if(node is None) :
                return res
            
            # Set the state
            acc.append(str(node.val))

            if(not node.left and not node.right) :
                res.append('->'.join(acc))
            else :
                # Go to next state
                helper(node.left, acc, res)
                helper(node.right, acc, res)

            # Reset the state
            acc.pop()

            return res
        
        ans = helper(root, [], [])
        return ans