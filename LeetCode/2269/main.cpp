class Solution {
public:
    int divisorSubstrings(int num, int k) {
        
        string s = to_string(num);
        int n = s.length();
        int ans = 0;
        
        for(int i = 0; i + k <= n; i++) {
            int d = stoi(s.substr(i, k));
            if(d != 0 && num % d == 0) {
                ans++;
            }
        }

        return ans;

    }
};