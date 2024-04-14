class Solution {
public:
  string simplifyPath(string s) {

    stringstream ss(s);
    string token;
    string ans = "";

    stack<string> st;

    while (getline(ss, token, '/')) {
      cout << token << "\n";

      // ignore blank space and single dot (cur dir)
      if (token == "" || token == ".") {
        continue;
      }

      if (token == "..") {
        if (!st.empty()) {
          st.pop();
        }
      } else {
        st.push(token);
      }
    }

    while (!st.empty()) {
      ans = "/" + st.top() + ans;
      st.pop();
    }

    return (ans.length() == 0) ? "/" : ans;

    return token;
  }
};