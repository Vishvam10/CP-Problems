#include <stack>
#include <string>

using namespace std;

string postToInfix(string s) {
  stack<string> st;

  for (char ch : s) {
    if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^') {
      string op1 = st.top();
      st.pop();
      string op2 = st.top();
      st.pop();
      string fstr = "(" + op2 + ch + op1 + ")";
      st.push(fstr);
    } else {
      string temp;
      temp += ch;
      st.push(temp);
    }
  }
  return st.top();
}