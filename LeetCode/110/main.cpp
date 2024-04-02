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
  int maxDepth(TreeNode *node, bool &balanced) {
    if (!node) {
      return 0;
    }
    int leftHeight = maxDepth(node->left, balanced);
    int rightHeight = maxDepth(node->right, balanced);
    if (abs(leftHeight - rightHeight) > 1) {
      balanced = false;
    }
    return 1 + max(leftHeight, rightHeight);
  }

  bool isBalanced(TreeNode *root) {
    bool ans = true;
    maxDepth(root, ans);
    return ans;
  }
};