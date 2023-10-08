void solve(string pref, int n, vector<string>& ans) {

    if(pref.length() == n) {
        ans.emplace_back(pref);
        return;
    }

    string temp;

    if(pref == "" || pref[pref.length()-1] == '0') {
        // Set the state 
        temp = pref + '0';

        // Goto next state
        solve(temp, n, ans);

        // Set the state
        temp = pref + '1';

        // Goto next state
        solve(temp, n, ans);

    } else {
        // Set the state
        temp = pref + '0';

        // Goto next state
        solve(temp, n, ans);
    }

}

vector<string> generateString(int n) {
    vector<string> ans;
    string pref = "";
    solve(pref, n, ans);
    sort(ans.begin(), ans.end())

    return ans;

}