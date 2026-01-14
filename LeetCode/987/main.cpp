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

    typedef vector<vector<int>> vec2d;

    // nodes := {value, x, y}

    void traverse(TreeNode* node, int x, int y, vec2d& nodes) {
        if(node == nullptr) return;
        nodes.push_back({node->val, x, y});
        traverse(node->left, x + 1, y - 1, nodes);
        traverse(node->right, x + 1, y + 1, nodes);
    }

    vec2d verticalTraversal(TreeNode* root) {
        vec2d nodes, ans;
        traverse(root, 0, 0, nodes);

        // First, we need to get ALL nodes having y = min, min - 1, 
        // min - 2, etc. Then sort by x and arrange ? And if same, 
        // secondary sort on val ?

        auto cmp = [](const vector<int>& a, const vector<int>& b) {
            if (a[2] != b[2]) return a[2] < b[2];
            if (a[1] != b[1]) return a[1] < b[1];
            return a[0] < b[0];
        };

        sort(nodes.begin(), nodes.end(), cmp);
        int prev = nodes[0][2];

        ans.push_back({nodes[0][0]});
        int ansPtr = 0;

        for(int i = 1; i < nodes.size(); ++i) {
            vector<int> val = nodes[i];
            int y = val[2];
            if(prev == y) {
                ans[ansPtr].emplace_back(val[0]);
            } else {
                ans.push_back({val[0]});
                ansPtr++;
                prev = y;
            }
        }

        return ans;

    }
};