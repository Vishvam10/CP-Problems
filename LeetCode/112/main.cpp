/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    bool check(TreeNode* node, int target) {
        if(node == nullptr) {
            return false;
        }

        if(node->left == nullptr && node->right == nullptr && target - node->val == 0) {
            return true;
        }

        bool left = check(node->left, target - node->val);
        bool right = check(node->right, target - node->val);

        return left || right;

    }

    bool hasPathSum(TreeNode* root, int targetSum) {
        if(root == nullptr && targetSum == 0) {
            return false;
        }
        return check(root, targetSum);
    }
};