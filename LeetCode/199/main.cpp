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
  vector<int> solve(TreeNode *node) {

    vector<int> ans;

    queue<TreeNode *> q;
    q.push(node);

    while (!q.empty()) {

      int sz = q.size();

      for (int i = 0; i < sz; i++) {
        TreeNode *cur = q.front();

        if (i == sz - 1) {
          ans.emplace_back(cur->val);
        }
        if (cur->left) {
          q.push(cur->left);
        }
        if (cur->right) {
          q.push(cur->right);
        }

        q.pop();
      }
    }

    return ans;
  }

  vector<int> rightSideView(TreeNode *root) {
    if (root == nullptr) {
      return vector<int>{};
    }
    return solve(root);
  }
};