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
  bool solve(TreeNode *node, int target, unordered_map<int, bool> &mp) {
    if (node == nullptr) {
      return false;
    }

    if (mp.find(target - node->val) != mp.end()) {
      return true;
    }

    mp[node->val] = true;

    bool left = solve(node->left, target, mp);
    bool right = solve(node->right, target, mp);

    return left || right;
  }

  bool findTarget(TreeNode *root, int k) {
    if (root == nullptr) {
      return false;
    }
    unordered_map<int, bool> mp;
    bool ans = solve(root, k, mp);
    return ans;
  }
};