class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& arr) {
        int n = arr.size();
        int c = 0, ans = 0;

        for(int i = 0; i < n; i++) {
            if(arr[i] == 1) {
                c += 1;
            } else {
                ans = max(ans, c);
                c = 0;
            }
        }

        ans = max(ans, c);

        return ans;

    }
};