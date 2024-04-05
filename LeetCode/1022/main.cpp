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

    int solve(TreeNode* node, int ans) {
        
        if(node == NULL) {
            return 0;
        }

        ans = ans * 2 + node->val;

        if(node->left == NULL && node->right == NULL) {
            return ans;
        }

        int left = solve(node->left, ans);
        int right = solve(node->right, ans);

        return left + right;

    }
   
    int sumRootToLeaf(TreeNode* root) {
        int ans = solve(root, 0);
        return ans;
    }
};