class Solution {
public:
    int longestAlternatingSubarray(vector<int>& arr, int threshold) {
        int c = 0, ans = 0, prev = 0;
        for(int num: arr) {
            if (c > 0 && (prev & 1) != (num & 1) && threshold >= num) {
                c++;
            } else {
                // if(threshold >= num && num & 1) {
                //     // if num is even, start with 1
                //     c = 1;
                // } else {
                //     // if num is odd, start with 0
                //     c = 0;
                // }
                c = ((num & 1) == 0 && threshold >= num);
            }
            ans = max(ans, c);
            prev = num;
        }
        return ans;
    }
};