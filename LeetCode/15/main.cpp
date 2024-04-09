class Solution {
 public:
    vector<vector<int>> threeSum(vector<int>& arr) {
        vector<vector<int>> ans;
        unordered_map<int, int> mp;
        sort(arr.begin(), arr.end());    
        
        int n = arr.size();
        
        if (n < 3) {
            return {};
        }
        if (arr[0] > 0) {
            return {};
        }
        
        for (int i = 0; i < n; i++) {
            mp[arr[i]] = i;
        }
        
        for (int i = 0; i < n - 2; i++) {
            if (i != 0 && arr[i] == arr[i - 1]) {
                continue;
            }
            
            for (int j = i + 1; j < n - 1; j++) {
                
                if (j != i + 1 && arr[j] == arr[j - 1]) {
                    continue;
                } 
                
                int key = -(arr[i] + arr[j]);
                if (mp.find(key) != mp.end() && mp[key] > j) {
                    ans.push_back({arr[i], arr[j], key});
                }
            }
        }
        return ans;
    }
};