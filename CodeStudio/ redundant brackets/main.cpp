#include <bits/stdc++.h>

bool findRedundantBrackets(string &s) {
  stack<char> st;

  // ignore characters except ( and )
  // if ) and we find ( before any operators,
  // we say it's redundant

  // ((a + b))          := ()   := we find (). so, redundant
  // (a + (b) / c)      := (+() := we find (). so redundant
  // (a*b + (c / d))    := "".  := we didn't find (). so, no redundant

  for (int i = 0; i < s.length(); i++) {
    char ch = s[i];
    if (ch == '(' || ch == '+' || ch == '-' || ch == '*' || ch == '/') {
      st.push(ch);
    } else {
      if (ch == ')') {
        bool flag = true;
        while (st.top() != '(') {
          char top = st.top();
          if (top == '+' || top == '-' || top == '*' || top == '/') {
            flag = false;
          }
          st.pop();
        }

        if (flag == true) {
          return true;
        }
        st.pop();
      }
    }
  }
  return false;
}