class Solution {
public:
    int longestOnes(vector<int>& arr, int k) {
        int n = arr.size();
        int left = 0, c = 0, ans = 0;

        for(int i = 0; i < n; i++) {
            if(arr[i] == 0) {
                c++;
            } 

            while(c > k) {
                if(arr[left] == 0) {
                    c--;
                }
                left++;
            }

            ans = max(ans, i - left + 1);

        }

        return ans;

    }
};