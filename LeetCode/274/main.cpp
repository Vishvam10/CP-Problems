class Solution {
public:
    int hIndex(vector<int>& arr) {
        int n = arr.size();
        int ans = 0;

        sort(arr.begin(), arr.end());

        for(int i = 0; i < n; i++) {
            int key = arr[i];
            int val = n - i;
            if(val >= key && key >= ans) {
                ans = max(ans, key);
            }
        }

        return ans;

    }
};