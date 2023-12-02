class Solution {
public:
    vector<int> runningSum(vector<int>& arr) {
        int n = arr.size();
        vector<int> ans;
        ans[0] = arr[0];
        for(int i = 1 ; i < n; i++) {
            ans[i] = ans[i-1] + arr[i];
        }
        return ans;
    }
}; 