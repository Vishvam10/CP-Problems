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
    vector<double> averageOfLevels(TreeNode* root) {

        if(root->left == NULL && root->right == NULL) {
            return vector<double> {static_cast<double>(root->val)};
        }
        queue<TreeNode*> q;
        vector<double> ans;
        q.emplace(root);

        while(!q.empty()) {
           
            double sz = q.size();
            double s = 0;

            for(int i = 0; i < sz; i++) {
                TreeNode* node = q.front();
                q.pop();

                s += node->val;

                if(node->left) {
                    q.push(node->left);
                }
                if(node->right) {
                    q.push(node->right);
                }
                
            }

            ans.emplace_back(s / sz);

        };

        return ans;

    }
};