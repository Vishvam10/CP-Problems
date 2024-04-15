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
  unordered_map<int, int> mp;

  TreeNode *build(vector<int> &inorder, vector<int> &postorder, int is, int ie,
                  int ps, int pe) {
    if (is > ie || ps > pe) {
      return nullptr;
    }

    TreeNode *node = new TreeNode(postorder[pe]);
    int ind = mp[postorder[pe]];
    int leftSubtreeSize = ind - is;

    node->left =
        build(inorder, postorder, is, ind - 1, ps, ps + leftSubtreeSize - 1);
    node->right =
        build(inorder, postorder, ind + 1, ie, ps + leftSubtreeSize, pe - 1);

    return node;
  }

  TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {

    int n = postorder.size();

    for (int i = 0; i < n; i++) {
      mp[inorder[i]] = i;
    }

    return build(inorder, postorder, 0, n - 1, 0, n - 1);
  }
};