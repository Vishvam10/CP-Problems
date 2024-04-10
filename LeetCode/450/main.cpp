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
  TreeNode *solve(TreeNode *node) {

    if (node->left == nullptr) {
      return node->right;
    } else if (node->right == nullptr) {
      return node->left;
    } else {

      // find inorder successor (largest in left child)
      // it could also be the smallest in right child in
      // which case the pointer assignment would be the opposite

      TreeNode *temp = node->left;
      while (temp->right != nullptr) {
        temp = temp->right;
      }

      temp->right = node->right;
      return node->left;
    }
  }

  TreeNode *deleteNode(TreeNode *root, int k) {

    if (root == nullptr) {
      return root;
    }

    if (root->val == k) {
      TreeNode *node = solve(root);
      return node;
    }

    // find the node
    TreeNode *temp = root;

    // if (root->left) or (root->right) check fails,
    // we just come out of the loop and return the
    // unmodified tree since the key is not present
    while (root != nullptr) {

      if (root->val > k) {
        if (root->left && root->left->val == k) {
          root->left = solve(root->left);
          break;
        } else {
          root = root->left;
        }
      } else {
        if (root->right && root->right->val == k) {
          root->right = solve(root->right);
          break;
        } else {
          root = root->right;
        }
      }
    }

    return temp;
  }
};