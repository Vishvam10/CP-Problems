/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
  void nodeDepth(TreeNode *node, int target, int depth, int &ans,
                 TreeNode *prev, TreeNode *&parent) {
    if (node == nullptr) {
      return;
    }
    if (node->val == target) {
      ans = depth;
      parent = prev;
      return;
    }
    nodeDepth(node->left, target, depth + 1, ans, node, parent);
    nodeDepth(node->right, target, depth + 1, ans, node, parent);
    return;
  }

  bool isCousins(TreeNode *root, int x, int y) {
    int d1, d2;
    TreeNode *p1, *p2;
    nodeDepth(root, x, 0, d1, nullptr, p1);
    nodeDepth(root, y, 0, d2, nullptr, p2);

    return d1 == d2 && p1 != p2;
  }
};