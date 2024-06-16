class Solution {
public:

    typedef vector<int> vec;
    typedef vector<vector<int>> vec2d;

    string s;
    string p;

    bool solve(int p1, int p2, vec2d& cache) {

        if (p2 == p.length()) {
            return p1 == s.length();
        }

        if(cache[p1][p2] != -1) {
            return cache[p1][p2];
        }

        // consider '.' to be a match
        bool match = (p1 < s.length() && (s[p1] == p[p2] || p[p2] == '.'));

        /*  
            to handle the '*' operator, either :
                - ignore '*' and move to next element in pattern or
                - use '*' to match current character in s and proceed
        */

        if (p2 + 1 < p.length() && p[p2 + 1] == '*') {

            bool skip = solve(p1, p2 + 2, cache);
            bool pick = match && solve(p1 + 1, p2, cache);

            return cache[p1][p2] = solve(p1, p2 + 2, cache) || (match && solve(p1 + 1, p2, cache));

        } 

        return cache[p1][p2] = (match && solve(p1 + 1, p2 + 1, cache));

    }

    bool isMatch(string _s, string _p) {
        s = _s;
        p = _p;

        int n = s.length();
        int m = p.length();

        vec2d cache(n + 1, vec(m + 1, -1));
        return solve(0, 0, cache);

    }
};