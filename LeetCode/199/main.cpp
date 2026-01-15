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
    vector<int> rightSideView(TreeNode* root) {
        if(root == nullptr) return {};

        vector<int> ans;
        queue<TreeNode*> q;
        q.push(root);

        // Level order traversal
        while(!q.empty()) {

            int sz = q.size();
            int visible = 0;
            for(int i = 0; i < sz; ++i) {

                TreeNode* node = q.front();
                q.pop();
                visible = node->val;

                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);

            }

            // At each level, only 1 will be visible and that's the last
            // one added
            ans.emplace_back(visible);
        }
        return ans;
    }
};