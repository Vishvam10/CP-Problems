class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& arr, int m, int n) {
        
        if(arr.size() != m * n) {
            return vector<vector<int>> ();
        }

        vector<vector<int>> mat(m, vector<int> (n, 0));

        int row = 0;
        for(int i = 0; i < arr.size(); i++) {
            if(i != 0 && i % n == 0) {
                row++;
            }
            mat[row][i % n] = arr[i];
        }
        
        return mat;

    }
};