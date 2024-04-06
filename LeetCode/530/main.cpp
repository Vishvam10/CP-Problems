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

    TreeNode* prev = nullptr;
    int ans = INT_MAX;

    void travel(TreeNode* node) {

        if(node == nullptr) {
            return;
        }

        travel(node->left);

        if(prev != nullptr) {
            ans = min(ans, abs(node->val - prev->val));
        }

        prev = node;

        travel(node->right);
        return;

    }

    int getMinimumDifference(TreeNode* root) {
        travel(root);
        return ans;        
    }
};