#include <string>
#include <vector>

/**
 * Definition for a binary tree node
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
  void helper(TreeNode *node, string acc, vector<string> &res) {

    if (acc.size() > 0) {
      acc += ("->" + to_string(node->val));
    } else {
      acc += to_string(node->val);
    }

    if (!node->left && !node->right) {
      res.emplace_back(acc);
    }

    if (node->left) {
      helper(node->left, acc, res);
    }
    if (node->right) {
      helper(node->right, acc, res);
    }
  }

  vector<string> binaryTreePaths(TreeNode *root) {
    vector<string> res;
    helper(root, "", res);
    return res;
  }
};