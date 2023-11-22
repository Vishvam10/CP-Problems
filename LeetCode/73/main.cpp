class Solution {
public:
    void setZeroes(vector<vector<int>>& mat) {
        int n = mat.size();
        int m = mat[0].size();
        bool flag_row = false, flag_col = false;
        
        // Instead of these, we will use the first row and 
        // first column the matrix itself to store that info
        // int rows[n], cols[m];

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(mat[i][j] == 0) {
                    if(i == 0) {
                        flag_row = true;
                    }
                    if(j == 0) {
                        flag_col = true;
                    }
                    mat[0][j] = 0;
                    mat[i][0] = 0;
                }
            }
        }

        for(int i = 1; i < n; i++) {
            for(int j = 1; j < m; j++) {
                if(mat[i][0] == 0 || mat[0][j] == 0) {
                    mat[i][j] = 0;
                }
            }
        }

        if(flag_row) {
            for(int i = 0; i < m; i++) {
                mat[0][i] = 0;
            }
        }

        if(flag_col) {
            for(int i = 0; i < n; i++) {
                mat[i][0] = 0;
            }
        }
        
    }
};


/*
    O(N + M) space

    void setZeroes(vector<vector<int>>& mat) {
        int n = mat.size();
        int m = mat[0].size();

        int rows[n], cols[m];

        // Initialize all the elements to 0
        memset(rows, 0, sizeof(rows));
        memset(cols, 0, sizeof(cols));

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(mat[i][j] == 0) {
                    rows[i] = 1;
                    cols[j] = 1;
                }
            }
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(rows[i] == 1 || cols[j] == 1) {
                    mat[i][j] = 0;
                }
            }
        }   
    }

    
*/ 