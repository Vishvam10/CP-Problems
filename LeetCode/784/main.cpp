class Solution {
public:

    vector<string> ans;

    void helper(string& str, int pos) {
        if(pos == str.length()) {
            ans.emplace_back(str);
            return;
        }

        if(!isalpha(str[pos])) {
            helper(str, pos + 1);
        } else if(islower(str[pos])) {
            helper(str, pos + 1);
            str[pos] = toupper(str[pos]);
            helper(str, pos + 1);
        } else {
            helper(str, pos + 1);
            str[pos] = tolower(str[pos]);
            helper(str, pos + 1);
        }

        return;

    } 

    vector<string> letterCasePermutation(string s) {
        helper(s, 0);
        return ans;
    }   
};