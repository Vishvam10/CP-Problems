/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// optimized solution

class Solution {
public:

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
        while(root != nullptr) {
            if(root->val < p->val && root->val < q->val) {
                // same direction, so move common ptr
                root = root->right;
            } else if(root->val > p->val && root->val > q->val) {
                // same direction, so move common ptr
                root = root->left;
            } else {
                // diverges, so return the point of divergence
                return root;
            }
        }

        // same node basically
        return nullptr;        

    }
};


// naive solution

class Solution {
public:

    void solve(TreeNode* node, vector<TreeNode*>& path, int target) {
        if(node == nullptr) {
            return;
        }
        path.emplace_back(node);
        if(node->val < target) {
            solve(node->right, path, target);
        } else if(node->val > target){
            solve(node->left, path, target);
        } 
        return;
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
        vector<TreeNode*> path1;
        vector<TreeNode*> path2;

        TreeNode* ans = nullptr;

        solve(root, path1, p->val);
        solve(root, path2, q->val);

        for(int i = 0; i < min(path1.size(), path2.size()); i++) {
            if(path1[i]->val == path2[i]->val) {
                ans = path1[i];
            }
        }

        return ans;

    }
};


