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
  void travel(TreeNode *node, vector<int> &res) {
    if (node == nullptr) {
      return;
    }
    travel(node->left, res);
    res.emplace_back(node->val);
    travel(node->right, res);
  }

  void merge(vector<int> &arr1, vector<int> &arr2, vector<int> &res) {
    int n = arr1.size();
    int m = arr2.size();

    int i = 0, j = 0;

    while (i < n && j < m) {
      if (arr1[i] < arr2[j]) {
        res.emplace_back(arr1[i]);
        i++;
      } else {
        res.emplace_back(arr2[j]);
        j++;
      }
    }

    while (i < n) {
      res.emplace_back(arr1[i]);
      i++;
    }

    while (j < m) {
      res.emplace_back(arr2[j]);
      j++;
    }

    return;
  }

  vector<int> getAllElements(TreeNode *root1, TreeNode *root2) {

    vector<int> arr1;
    vector<int> arr2;
    vector<int> arr3;

    travel(root1, arr1);
    travel(root2, arr2);
    merge(arr1, arr2, arr3);

    return arr3;
  }
};