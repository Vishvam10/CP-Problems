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
  void leaves(TreeNode *node, vector<int> &res) {
    if (node->left == nullptr && node->right == nullptr) {
      res.emplace_back(node->val);
      return;
    }
    if (node->left) {
      leaves(node->left, res);
    }
    if (node->right) {
      leaves(node->right, res);
    }
  }

  bool leafSimilar(TreeNode *root1, TreeNode *root2) {

    vector<int> res1, res2;
    leaves(root1, res1);
    leaves(root2, res2);

    if (res1.size() != res2.size()) {
      return false;
    }

    // return equal(res1.begin(), res1.end(), res2.begin(), res2.end());
    return res1 == res2;
  }
};