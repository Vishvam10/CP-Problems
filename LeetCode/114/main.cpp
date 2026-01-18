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

    void solve(TreeNode* node, TreeNode*& head) {
        if(node == nullptr) return;

        head->right = node;
        head->left = nullptr;

        TreeNode* left = node->left;
        TreeNode* right = node->right;

        head = head->right;

        solve(left, head);
        solve(right, head);
    }

    void flatten(TreeNode* root) {
        TreeNode dummy{0, nullptr, nullptr};
        TreeNode* head = &dummy;
        solve(root, head);
        root = head;
    }
};