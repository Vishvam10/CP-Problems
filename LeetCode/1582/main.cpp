class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        int ans = 0;
        vector<int> rows(m), cols(n);

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                rows[i] += mat[i][j];
                cols[j] += mat[i][j];
            }
        }
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) 
                ans += (rows[i] == 1 && cols[j] == 1 && mat[i][j] == 1);
        }
        return ans;
    }
};