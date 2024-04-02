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

    if (!root) {
      return vector<vector<int>>{};
    }

    queue<TreeNode *> q;
    vector<vector<int>> ans;
    bool ltr = true;

    q.push(root);

    while (!q.empty()) {

      int sz = q.size();

      vector<int> temp(sz);

      for (int i = 0; i < sz; i++) {

        TreeNode *node = q.front();
        q.pop();

        temp[i] = node->val;

        if (node->left) {
          q.push(node->left);
        }
        if (node->right) {
          q.push(node->right);
        }
      }

      if (!ltr) {
        reverse(temp.begin(), temp.end());
        ltr = true;
      } else {
        ltr = false;
      }

      ans.emplace_back(temp);
    }

    return ans;
  }
};