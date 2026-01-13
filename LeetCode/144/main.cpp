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
  void traverse(TreeNode *node, vector<int> &ans) {
    if (node == nullptr) {
      return;
    }
    if (node->left) {
      ans.emplace_back(node->left->val);
      traverse(node->left, ans);
    }
    if (node->right) {
      ans.emplace_back(node->right->val);
      traverse(node->right, ans);
    }
  }

  vector<int> preorderTraversal(TreeNode *root) {
    if (root == nullptr) {
      return {};
    }
    vector<int> ans;
    ans.emplace_back(root->val);
    traverse(root, ans);
    return ans;
  }
};