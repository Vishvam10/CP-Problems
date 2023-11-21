class Solution {
public:
    int mostWordsFound(vector<string>& arr) {
        int ans = 0;
        for(string& s : arr) {
            int c = count(s.begin(), s.end(), ' ');
            ans = max(ans, c);
        }
        return ans + 1;
    }
};