#include <algorithm>
#include <bits/stdc++.h>
#include <climits>
#include <vector>

using namespace std;

/* TYPES  */
#define ll long long
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vi vector<int>
#define vll vector<long long>
#define mii map<int, int>
#define si set<int>
#define sc set<char>

/* FUNCTIONS */
#define f(i, s, e) for (long long int i = s; i < e; i++)
#define cf(i, s, e) for (long long int i = s; i <= e; i++)
#define rf(i, e, s) for (long long int i = e - 1; i >= s; i--)
#define pb push_back
#define eb emplace_back

/* PRINTS */
template <class T> void print_v(vector<T> &v) {
  cout << "\n";
  for (auto x : v) {
    cout << x << " ";
  }
  cout << "\n";
}

template <class T> void print_v2d(vector<vector<T>> &v) {
  cout << "\n";
  for (auto x : v) {
    for (auto y : x) {
      cout << y << " ";
    }
    cout << "\n";
  }
  cout << "\n";
}

/* UTILS */
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795
#define read(type) readInt<type>()

ll min(ll a, int b) {
  if (a < b)
    return a;
  return b;
}

ll min(int a, ll b) {
  if (a < b)
    return a;
  return b;
}

ll max(ll a, int b) {
  if (a > b)
    return a;
  return b;
}

ll max(int a, ll b) {
  if (a > b)
    return a;
  return b;
}

ll gcd(ll a, ll b) {
  if (b == 0)
    return a;
  return gcd(b, a % b);
}

ll lcm(ll a, ll b) { return a / gcd(a, b) * b; }

string to_upper(string a) {
  for (int i = 0; i < (int)a.size(); ++i)
    if (a[i] >= 'a' && a[i] <= 'z')
      a[i] -= 'a' - 'A';
  return a;
}

string to_lower(string a) {
  for (int i = 0; i < (int)a.size(); ++i)
    if (a[i] >= 'A' && a[i] <= 'Z')
      a[i] += 'a' - 'A';
  return a;
}

bool prime(ll a) {
  if (a == 1)
    return 0;
  for (int i = 2; i <= round(sqrt(a)); ++i)
    if (a % i == 0)
      return 0;
  return 1;
}

void yes() { cout << "YES\n"; }
void no() { cout << "NO\n"; }

/*  All Required define Pre-Processors and typedef Constants */
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int uint64;

void FastIO() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
}

void solve1() {

  int n;
  cin >> n;

  string s;
  cin >> s;

  // No. of perms = n! / (a1! * a2! * ... * an!) where ai is a group of same
  // characters ... we want to minimize this. n is fixed, so we need to maximise
  // the denominator ... increasing max(a1, a2, .., an) by 1 and decreasing
  // min(a1, a2, ..., an) by 1 (by 1 because no. of ops allowed is 1) would be
  // the best. min = 1 is also taken care ? As 0! = 1 ...

  // char -> (first index, freq)
  unordered_map<char, pair<int, int>> mp;
  int mx = INT_MIN, mn = INT_MAX;
  int mxi = -1, mni = -1;

  for (int i = 0; i < n; ++i) {
    if (mp.find(s[i]) == mp.end()) {
      mp[s[i]] = {i, 0};
    } else {
      mp[s[i]].second++;
    }
  }

  for (auto it = mp.begin(); it != mp.end(); ++it) {
    int index = it->second.first;
    int freq = it->second.second;

    if (freq > mx) {
      mx = freq;
      mxi = index;
    }

    if (freq < mn) {
      mn = freq;
      mni = index;
    }
  }

  cout << "debug : " << mxi << ", " << mni << "\n";

  s[mni] = s[mxi];

  cout << s << "\n";

  return;
}

int main() {
  FastIO();
  int tc;
  cin >> tc;
  for (int t = 1; t <= tc; t++) {
    solve();
  }
}