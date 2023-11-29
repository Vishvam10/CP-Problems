class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int n = arr.size();
        int left = 0, ans = 0, s = 0;

        for(int i = 0; i < k; i++) {
            s += arr[i];
        }

        for(int i = k + 1; i < n; i++) {
            s += arr[i];
            if(s / k >= threshold) {
                ans++;
            }
            s -= arr[left];
            left++;
        }
        return ans;
    }
};