"""
DIFFICULTY : medium
TAGS : tree, bfs, binary tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        depth = 0
        queue = []
        queue.append(root)
        ans = []
        while queue:
            # depth += 1
            temp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            ans.append(temp)

        return ans
