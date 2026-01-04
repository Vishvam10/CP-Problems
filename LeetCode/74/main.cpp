class Solution {
public:

    bool searchMatrix(vector<vector<int>>& mat, int target) {
        int nrows = mat.size(), ncols = mat[0].size();

        // Here we can simply use BS on 1st col to find the starting
        // point then BS on that corresponding row. We can do this
        // as it guaranteed that the first integer of each row is greater 
        // than the last integer of the previous row.

        // BS on column
        int low = 0, high = nrows - 1, mid = 0, reqRow = -1;
        while(low <= high) {

            mid = low + (high - low) / 2;
            if(mat[mid][0] == target) {
                return true;
            } else if(mat[mid][0] < target) {
                low = mid + 1;
                reqRow = mid;
            } else {
                high = mid - 1;
            }
        }

        if (reqRow == -1)
            return false;

        // BS on row (= mid)
        low = 0, high = ncols - 1, mid = 0;
        while(low <= high) {
            mid = low + (high - low) / 2;
            if(mat[reqRow][mid] == target) {
                return true;
            } else if(mat[reqRow][mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return false;
        
    }
};