class Solution {
public:
    int maximumWealth(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        int ans = 0;

        for(int i = 0; i < m; i++) {
            int s = 0;
            for(int j = 0; j < n; j++) {
                s += mat[i][j];
            }
            ans = max(ans, s);
        }

        return ans;

    }
};