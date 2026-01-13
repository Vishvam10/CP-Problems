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
  vector<vector<int>> zigzagLevelOrder(TreeNode *root) {

    if (root == nullptr)
      return {};

    vector<vector<int>> ans;
    queue<TreeNode *> q;
    q.push(root);
    bool flag = true;

    while (!q.empty()) {

      int sz = q.size();
      vector<int> levels;

      for (int i = 0; i < sz; ++i) {
        TreeNode *node = q.front();
        q.pop();
        levels.emplace_back(node->val);
        if (node->left) {
          q.push(node->left);
        }
        if (node->right) {
          q.push(node->right);
        }
      }

      if (flag) {
        ans.emplace_back(levels);
      } else {
        ans.emplace_back(levels.rbegin(), levels.rend());
      }

      flag = !flag;
    }

    return ans;
  }
};