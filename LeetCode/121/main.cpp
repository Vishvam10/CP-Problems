class Solution {
public:
    int maxProfit(vector<int>& arr) {

        int n = arr.size();

        if(n == 1) {
            return 0;
        }

        int ans = INT_MIN;
        
        // for each elem : find max to right ...
        // suffix max maybe ?

        // 7 1 5 3 6 4
        // 7 6 6 6 6 4
        
        vector<int> suf(n, -1);
        suf[n - 1] = arr[n - 1];

        for(int i = n - 2; i >= 0; --i) {
            suf[i] = max(arr[i], suf[i + 1]);
        }

        for(int i = 0; i < n; ++i) {
            ans = max(ans, suf[i] - arr[i]);
        }

        return ans;
        
    }
};