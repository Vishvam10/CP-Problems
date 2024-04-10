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
  int ans = 0;

  void solve(TreeNode *node, int low, int high) {
    if (node == nullptr) {
      return;
    }
    // if(node->val >= low && node->val <= high) {
    //     ans += node->val;
    //     solve(node->left, low, high);
    //     solve(node->right, low, high);
    // } else if(node->val < low) {
    //     solve(node->right, low, high);
    // } else if (node->val > high) {
    //     solve(node->left, low, high);
    // }

    // much better
    if (node->val >= low && node->val <= high) {
      ans += node->val;
    }
    if (node->left) {
      solve(node->left, low, high);
    }
    if (node->right) {
      solve(node->right, low, high);
    }

    return;
  }

  int rangeSumBST(TreeNode *root, int low, int high) {
    solve(root, low, high);
    return ans;
  }
};