class NumMatrix {
private:
    int n, m;
    vector<vector<int>> pref;
public:
    NumMatrix(vector<vector<int>> &mat) {
        n = mat.size();
        m = n > 0 ? mat[0].size() : 0;

        // Offset everything by 1 so that we don't
        // have to tackle the edge cases (1st row and 
        // col while init and row or col becoming negative)
        pref = vector<vector<int>>(n + 1, vector<int>(m+1, 0));
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= m; j++) {
                pref[i][j] = mat[i-1][j-1] + 
                             pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] ;
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        return pref[row2+1][col2+1] - pref[row2+1][col1] - pref[row1][col2+1] + pref[row1][col1];
    }
};