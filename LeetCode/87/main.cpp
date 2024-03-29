class Solution {
public:
  int evalRPN(vector<string> &arr) {
    int n = arr.size();
    stack<int> st;

    for (int i = 0; i < n; i++) {
      string ch = arr[i];

      if (ch.length() == 1 && int(ch[0]) < 48) {
        int b = st.top();
        st.pop();
        int a = st.top();
        st.pop();
        if (ch == "+") {
          st.push(a + b);
        } else if (ch == "-") {
          st.push(a - b);
        } else if (ch == "*") {
          st.push(a * b);
        } else if (ch == "/") {
          st.push(a / b);
        }

      } else {
        int num = stoi(ch);
        st.push(num);
      }
    }
    return st.top();
  }
};