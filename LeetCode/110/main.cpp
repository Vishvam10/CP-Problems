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
  int check(TreeNode *node) {
    if (node == nullptr) {
      return 0;
    }

    int left = check(node->left);
    int right = check(node->right);

    if (left == -1 || right == -1 || abs(left - right) > 1) {
      return -1;
    }

    int ht = 1 + max(left, right);
    return ht;
  }

  bool isBalanced(TreeNode *root) {
    if (root == nullptr) {
      return true;
    }

    if (check(root) == -1) {
      return false;
    }

    return true;
  }
};