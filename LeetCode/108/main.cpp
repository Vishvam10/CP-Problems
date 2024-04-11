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

    TreeNode* construct(vector<int> arr, int low, int high) {

        if(low > high) {
            return nullptr;
        }

        int mid = low + (high - low) / 2;
        
        TreeNode* node = new TreeNode(arr[mid]);
        node->left = construct(arr, low, mid - 1);
        node->right = construct(arr, mid + 1, high);

        return node;
    }

    TreeNode* sortedArrayToBST(vector<int>& arr) {
        int n = arr.size();
        return construct(arr, 0, n - 1);
    }
};