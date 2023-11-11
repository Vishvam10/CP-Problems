class Solution {
public:
    vector<vector<int>> subsets(vector<int>& arr) {
        vector<vector<int>> ans;
        vector<int> temp;
        int bit_length = arr.size();
        int cardinality = 1 << bit_length;

        for(int i = 0; i < cardinality; i++) {
            temp.clear();
            for(int j = 0; j < bit_length; j++) {
                // Check if the jth bit of i is set
                // If so, include the number in that index
                if((i >> j) & 1) {
                    temp.emplace_back(arr[j]);
                }
            }
            ans.emplace_back(temp);
        }
        return ans;
    }
};