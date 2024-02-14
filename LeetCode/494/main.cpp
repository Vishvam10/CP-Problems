class Solution {
public:

    int ans = 0;

    void helper(vector<int>& arr, int ind, int res, int target) {
        
        if(res == target && ind == arr.size()) {
            ans++;
            return;
        } 

        if(ind >= arr.size()) {
            return;
        }

       
        // pick + 
        helper(arr, ind + 1, res + arr[ind], target);

        // pick -
        helper(arr, ind + 1, res - arr[ind], target);

        return;

    }

    int findTargetSumWays(vector<int>& arr, int target) {
        
        helper(arr, 0, 0, target);

        return ans;
    }
};