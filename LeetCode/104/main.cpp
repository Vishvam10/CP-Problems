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
  int md(TreeNode *node, int height) {
    if (node == nullptr) {
      return height;
    }
    int left = md(node->left, height + 1);
    int right = md(node->right, height + 1);
    return max(left, right);
  }

  int maxDepth(TreeNode *root) { return md(root, 0); }
};