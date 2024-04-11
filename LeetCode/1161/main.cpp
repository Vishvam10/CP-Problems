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
    int maxLevelSum(TreeNode* root) {

        int mx = INT_MIN;
        int level = 0;
        int ans = 0;
        
        queue<TreeNode*> q;
        q.push(root);

        while(!q.empty()) {

            int sz = q.size();
            int s = 0;
            
            level++;

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

            if(s > mx) {
                ans = level;
                mx = s;
            }

        }

        return ans;


    }
};