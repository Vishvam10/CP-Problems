class Solution {
public:
    bool areSimilar(vector<vector<int>>& mat, int k) {
        int m = mat.size();
        int n = mat[0].size();

        // for(int i = 0; i < m; i++) {
        //     for(int j = 0; j < n; j++) {
        //         if(i % 2 == 1) {
        //             // left shift
        //             // actually (j-k+n) % n but we do ((j-k)%n + n) % n to avoid overflow
        //             if(mat[i][j] != mat[i][((j-k)%n+n)%n]) {
        //                 return false;
        //             }
        //         } else {
        //             // right shift
        //             if(mat[i][j] != mat[i][(j+k)%n]) {
        //                 return false;
        //             }
        //         }
        //     }
        // }

        if(k % n == 0) {
            return true;
        }
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(mat[i][j] != mat[i][(j+k) % n]) {
                    return false;
                }
            }
        }

        return true;

    }
};