#include <bits/stdc++.h>
#include <string>
#include <vector>

vector<string> subsequences(string s) {

  int n = s.length();
  int p = 1 << n;
  vector<string> ans;
  string temp;

  // Starting from 1 so that the empty string is not included
  for (int i = 1; i < p; i++) {
    temp.clear();
    for (int j = 0; j < n; j++) {
      if ((i >> j) & 1) {
        temp += s[j];
      }
    }
    ans.emplace_back(temp);
  }

  return ans;
}
