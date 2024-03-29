#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll pref[3000005];

void solve() {
  ll n, ans = 0;
  cin >> n;

  for (int i = 1, x; i <= n; i++) {
    cin >> x;
    pref[i] = pref[i - 1] + x;
  }

  for (int i = 1; i <= n; i++) {
    if (n % i == 0) {
      ll mx = 0, mn = 2e18;
      for (ll j = i; j <= n; j += i) {
        mx = max(mx, pref[j] - pref[j - i]);
        mn = min(mn, pref[j] - pref[j - i]);
      }
      ans = max(ans, mx - mn);
    }
  }
  cout << ans << "\n";
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}