#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

void solve() {

  ll n, s = 0, p = 1;
  cin >> n;

  s = n * (n + 1) / 2;

  while (p <= n) {
    s -= (2 * p);
    p *= 2;
  }

  cout << s << "\n";

  return;
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}