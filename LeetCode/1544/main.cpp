class Solution {
public:
  string makeGood(string s) {

    int n = s.length();
    string ans;
    stack<char> st;

    for (int i = 0; i < n; i++) {
      char t = st.top();

      // same letter, lower and upper case
      if (!st.empty() && abs(t - s[i]) == 32) {
        st.pop();
      } else {
        st.push(s[i]);
      }
    }

    while (!st.empty()) {
      ans = st.top() + ans;
      st.pop();
    }

    return ans;
  }
};