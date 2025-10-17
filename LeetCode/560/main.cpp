class Solution {
public:
    int subarraySum(vector<int>& arr, int k) {

        // do two-sum on pref
        int n = arr.size();
        int s = 0, ans = 0;
        unordered_map<int, int> mp;

        mp[s] = 1;

        for(int i = 0; i < n; i++) {
            s += arr[i];
            int target = s- k;
            if(mp.find(target) != mp.end()) {
                ans += mp[target];
            }
            mp[s]++;
        }
        
        return ans;

    }
}; 