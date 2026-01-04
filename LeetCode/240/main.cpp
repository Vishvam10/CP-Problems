class Solution {
public:

    bool searchMatrix(vector<vector<int>>& mat, int target) {
        int nrows = mat.size(), ncols = mat[0].size();

        // BS on col then on row may not be as efficient as we
        // once we find the lower_bound - 1 col, we may have to check 
        // linearly on all cols upto that point. Take the first example
        // of 5 itself. It could be in col 0, 1 or 2

        // Hmm, (0,0) is the smallest and (nrow - 1, ncols - 1) is
        // the highest ... to generalize, the bottom right is always
        // the highest and top left is always the lowest ...

        // Maybe diagonally reduce the search space ?

        int row = 0, col = ncols - 1, ele = 0;

        while (row <= nrows - 1 && col >= 0) {
            ele = mat[row][col];
            if (ele == target) {
                return true;
            } else if (ele < target) {
                row++;
            } else {
                col--;
            }
        }

        // ... even then it's O(m + n) .. 

        return false;
        
    }
};