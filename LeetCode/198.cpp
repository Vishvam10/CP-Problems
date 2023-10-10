class Solution {
public:

    vector<int> mp;

    int solve(vector<int> arr, int ind) {
        if(ind < 0) {
            return 0;
        }
        if(mp[ind] >= 0) {
            return mp[ind];
        }

        int yes = arr[ind] + solve(arr, ind - 2);
        int no = solve(arr, ind - 1);
        int ans = max(yes, no);

        mp[ind] = ans;

        return ans;

    }

    int rob(vector<int>& arr) {
        
        int n = arr.size();
        for(int i=0; i<n; i++) {
            mp.emplace_back(-1);
        }
        int ans = solve(arr, n - 1);

        return ans;

    }
};