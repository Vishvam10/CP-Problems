class Solution {
public:
    int findPairs(vector<int>& arr, int k) {
        int n = arr.size(), ans = 0;
        int i = 0, j = 1, diff = 0;

        sort(arr.begin(), arr.end());

        while(j < n) {

            diff = abs(arr[j] - arr[i]);
            
            if(diff == k) {
                i++;
                j++;
                ans++;
                // skip duplicates
                while(j < n && arr[j] == arr[j-1]) {
                    j++;
                }
            } else if(i + 1 != j && diff > k) {  
                i++;
            } else {
                j++;
            }

        }

        return ans;

        
    }
};