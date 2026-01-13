/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool check(struct TreeNode* a, struct TreeNode* b) {

    if(a == NULL && b == NULL) {
        return true;
    }
    if(a == NULL || b == NULL) {
        return false;
    }
    if(a->val != b->val) {
        return false;
    }
    return check(a->left, b->right) && check(a->right, b->left);

}

bool isSymmetric(struct TreeNode* root) {
    if (root == NULL) return true;
    return check(root->left, root->right);
}