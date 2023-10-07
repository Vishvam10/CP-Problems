#include <bits/stdc++.h> 
/* 
Following is the structure of Tree Node:

class TreeNode
{   
    public:
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int val)
    {
        this->val = val;
        left = NULL;
        right = NULL;
    }
};
*/

int ht(TreeNode *node) {
    if(node == nullptr) {
        return 0;
    }

    int left = ht(node->left);
    int right = ht(node->right);
    int ans = 1 + max(left, right);

    return ans;
}

int maxHeightDifference(TreeNode *root) {
    
    if(root == nullptr) {
        return 0;
    }

    int lh = ht(root->left);
    int rh = ht(root->right);
    int diff = abs(rh - lh);

    int left = maxHeightDifference(root->left);
    int right = maxHeightDifference(root->right);

    int ans = max(diff, max(left, right));
    
    return ans;
}

