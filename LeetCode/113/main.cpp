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
  vector<vector<int>> ans;

  bool isLeaf(TreeNode *node) {
    return (node->left == nullptr) && (node->right == nullptr);
  }

  void solve(TreeNode *node, vector<int> path, int target) {
    if (node == nullptr) {
      return;
    }
    path.emplace_back(node->val);

    if (isLeaf(node)) {
      int s = accumulate(path.begin(), path.end(), 0);
      if (s == target) {
        ans.emplace_back(path);
      };
    }

    // even if it is a leaf, we go to left and right child
    // this will return nothing anyway, so it's fine
    solve(node->left, path, target);
    solve(node->right, path, target);
    path.pop_back();
    return;
  }

  vector<vector<int>> pathSum(TreeNode *root, int targetSum) {
    vector<int> path;
    solve(root, path, targetSum);
    return ans;
  }
};