class Solution {
public:

    int helper(vector<int>& arr, int k) {

        int n = arr.size();
        int left = 0, ans = 0;

        for(int i = 0; i < n; i++) {
            if(arr[i] % 2 == 1) {
                k--;
            }
            while(k < 0) {
                if(arr[left] % 2 == 1) {
                    k++;
                }
                left++;
            }
            ans += (i - left + 1);
        }

        return ans;
    }

    int numberOfSubarrays(vector<int>& arr, int k) {
        return helper(arr, k) - helper(arr, k - 1);
    }
};