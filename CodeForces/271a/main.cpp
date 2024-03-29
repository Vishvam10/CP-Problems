#include <bits/stdc++.h>
#include <iostream>

using namespace std;

bool unique(int n) {
  unordered_map<int, bool> mp;
  while (n) {
    int dig = n % 10;
    if (mp.find(dig) != mp.end()) {
      return false;
    } else {
      mp[dig] = true;
    }
    n /= 10;
  }
  return true;
}

int main() {
  bool flag = true;
  int n;
  cin >> n;

  while (flag) {
    n += 1;
    if (unique(n)) {
      cout << n;
      flag = false;
    }
  }

  return 0;
}
