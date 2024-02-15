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

    int ans = 0;

    void count(TreeNode* node, bool left) {
        if(node == nullptr) {
            return;
        }

        if(node->left == nullptr && node->right == nullptr) {
            if(left) {
                ans += node->val;
            }
            return;
        }

        count(node->left, true);
        count(node->right, false);

        return;

    }

    int sumOfLeftLeaves(TreeNode* root) {
        if(root == nullptr) {
            return 0;
        }
        count(root->left, true);
        count(root->right, false);
        return ans;
    }
};