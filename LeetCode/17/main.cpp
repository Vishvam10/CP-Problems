#include <unordered_map>
#include <vector>
#include <string>

class Solution {
public:

    unordered_map<char, string> mp = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };


    void solve(
        int ind, string pref, string digits, vector<string>& ans
    ) {
        if(ind >= digits.length()) {
            ans.emplace_back(pref);
            return;
        }

        string temp = mp[digits[ind]];
        for(int i = 0; i < temp.length(); i++) {
            solve(ind + 1, pref + temp[i], digits, ans);
        }

    }

    vector<string> letterCombinations(string digits) {

        vector<string> ans;
        string res = "";

        if(digits.length() == 0) {
            return {};
        }
        
        solve(0, res, digits, ans);
        return ans;

    }
};