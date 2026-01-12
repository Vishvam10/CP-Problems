#include <bits/stdc++.h>
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

#define vi vector<int>

void solve() {
  int d, n;
  cin >> n >> d;

  vi arr;

  arr.emplace_back(1);

  if (d % 3 == 0 || n >= 3) {
    arr.emplace_back(3);
  }

  if (d == 0 || d == 5) {
    arr.emplace_back(5);
  }

  // Divisibility rule for 7 : split the number into blocks of 3, get the sign
  // alternative sum for each block, if that sum is divisible by 7, the number
  // is divisible by 7

  // d == 7 is obvious, n >= 3 will always give blocks of length 6 with
  // alternating sum = 0, so there's that

  if (d == 7 || n >= 3) {
    arr.emplace_back(7);
  }

  // Calculating fact gives TLE. (a * b) mod n = (a mod n) * (b mod n)
  // Using that, (d * n!) mod 9 = (d mod 9) * (n! mod 9)
  // (n! mod 9) = (n mod 9) * ((n - 1) mod 9) * ...
  // If n >= 9, the above would be 0

  bool div9 = false;
  if (d % 9 == 0 || n >= 6) {
    div9 = true;
  }
  // This is to handle small n explicitly by computing d * n! % 9.
  else {
    int fact = 1;
    for (int i = 2; i <= n; i++) {
      fact = (fact * i) % 9;
    }
    if ((fact * (d % 9)) % 9 == 0) {
      div9 = true;
    }
  }

  if (div9) {
    arr.emplace_back(9);
  }

  for (int i = 0; i < arr.size(); i++) {
    cout << arr[i] << " ";
  }

  cout << "\n";
}

int main() {
  FastIO();
  int tc;
  cin >> tc;
  for (int t = 1; t <= tc; t++) {
    solve();
  }
}