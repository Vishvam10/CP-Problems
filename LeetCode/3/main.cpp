class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int left = 0;
        int ans = 0;
        vector<bool> vis(256, false); 

        for(int right = 0; right < n; ++right) {
            while(vis[s[right]]) {
                vis[s[left]] = false;
                left++;
            }
            vis[s[right]] = true;
            ans = max(ans, right - left + 1);
        }

        return ans;
    }
};
