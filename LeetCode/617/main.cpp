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

    void merge(TreeNode*& ans, TreeNode* node1, TreeNode* node2) {

        if(!node1 && !node2) {
            return;
        } 
        if(!node1) {
            ans = new TreeNode(node2->val, node2->left, node2->right);
            return;
        }
        if(!node2) {
            ans = new TreeNode(node1->val, node1->left, node1->right);
            return;
        }

        ans = new TreeNode(node1->val + node2->val);
        merge(ans->left, node1->left, node2->left);
        merge(ans->right, node1->right, node2->right);
        return;
    }

    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        
        TreeNode* ans = NULL;
        merge(ans, root1, root2);
        return ans;

    }
};