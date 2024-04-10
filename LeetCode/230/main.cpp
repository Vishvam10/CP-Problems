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
  TreeNode *ans = nullptr;

  void travel(TreeNode *node, int &k) {
    if (node == nullptr) {
      return;
    }

    travel(node->left, k);

    // at the smallest node
    k -= 1;

    if (k == 0) {
      ans = node;
      return;
    }

    travel(node->right, k);

    return;
  }

  int kthSmallest(TreeNode *root, int k) {
    travel(root, k);
    return ans->val;
  }
};