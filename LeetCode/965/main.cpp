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
  int val;
  int ans = true;

  void solve(TreeNode *node) {
    if (node == NULL) {
      return;
    }
    if (node->val != val) {
      ans = false;
    }
    solve(node->left);
    solve(node->right);
    return;
  }

  bool isUnivalTree(TreeNode *root) {
    val = root->val;
    solve(root);
    return ans;
  }
};