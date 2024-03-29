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
  int check(TreeNode *node1, TreeNode *node2) {
    // if(node1 == nullptr) {
    //     if(node2 == nullptr) {
    //         return true;
    //     }
    //     return false;
    // }
    // if(node2 == nullptr) {
    //     if(node1 == nullptr) {
    //         return true;
    //     }
    //     return false;
    // }
    if (node1 == nullptr && node2 == nullptr) {
      return true;
    }
    if (node1 == nullptr || node2 == nullptr) {
      return false;
    }
    if (node1->val != node2->val) {
      return false;
    }

    int left = check(node1->left, node2->left);
    int right = check(node1->right, node2->right);

    if (left == false || right == false) {
      return false;
    }

    return true;
  }

  bool isSameTree(TreeNode *p, TreeNode *q) { return check(p, q); }
};