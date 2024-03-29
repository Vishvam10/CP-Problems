class Solution {
public:

    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int left = 0;
        int ans = 0;
        unordered_map<char, int> mp;

        for(int i = 0; i < n; i++) {
            char ch = s[i];
            mp[ch]++;
            if(mp[ch] > 1) {
                while(mp[ch] > 1) {
                    mp[s[left]]--;
                    left++;
                }
            }
            ans = max(ans, i - left + 1);
        }

        return ans;
    
    }
};