class Solution {
public:
    int trap(vector<int>& arr) {
        
        int n = arr.size();
        int ans = 0;

        int lefts[n], rights[n];

        lefts[0] = arr[0];        
        rights[n-1] = arr[n-1];

        for(int i = 1; i < n; i++) {
            lefts[i] = max(lefts[i-1], arr[i]);
        }

        for(int i = n - 2; i >= 0; i--) {
            rights[i] = max(rights[i+1], arr[i]);
        }

        for(int i = 0; i < n; i++) {
            int height = min(lefts[i], rights[i]) - arr[i];
            ans += height;
        }

        return ans;

    }
};