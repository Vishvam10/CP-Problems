#include <iostream>  // for cin, cout
#include <vector>    // for vector
#include <algorithm> // for max, min, sort, etc.
#include <map>       // for map
#include <set>       // for set
#include <cmath>     // for sqrt, round
#include <string>    // for string operations
#include <limits>    // for numeric_limits if needed

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

#define debug(...) debug_print(#__VA_ARGS__, __VA_ARGS__)

/* PRINTS */
template <class T>
void print_v(vector<T> &v)
{
  cout << "\n";
  for (auto x : v)
  {
    cout << x << " ";
  }
  cout << "\n";
}

template <class T>
void print_v2d(vector<vector<T>> &v)
{
  cout << "\n";
  for (auto x : v)
  {
    for (auto y : x)
    {
      cout << y << " ";
    }
    cout << "\n";
  }
  cout << "\n";
}

#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

template <typename T>
void print_one(const string &name, const T &value)
{
  cout << name << " = " << value << ", ";
}

template <typename T, typename... Args>
void debug_print(const string &names, const T &value, const Args &...args)
{
  stringstream ss(names);
  string name;
  int paren_count = 0;

  while (getline(ss, name, ','))
  {
    if (paren_count == 0 || name.back() != ')')
      break;
  }

  // Remove leading spaces
  size_t first = name.find_first_not_of(" ");
  if (first != string::npos)
    name = name.substr(first);

  print_one(name, value);
  if constexpr (sizeof...(args) > 0)
  {
    auto rest_names = names.substr(names.find(',') + 1);
    debug_print(rest_names, args...);
  }
  else
  {
    cout << "\n";
  }
}

/* UTILS */
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795
#define read(type) readInt<type>()

ll min(ll a, int b)
{
  if (a < b)
    return a;
  return b;
}

ll min(int a, ll b)
{
  if (a < b)
    return a;
  return b;
}

ll max(ll a, int b)
{
  if (a > b)
    return a;
  return b;
}

ll max(int a, ll b)
{
  if (a > b)
    return a;
  return b;
}

ll gcd(ll a, ll b)
{
  if (b == 0)
    return a;
  return gcd(b, a % b);
}

ll lcm(ll a, ll b) { return a / gcd(a, b) * b; }

string to_upper(string a)
{
  for (int i = 0; i < (int)a.size(); ++i)
    if (a[i] >= 'a' && a[i] <= 'z')
      a[i] -= 'a' - 'A';
  return a;
}

string to_lower(string a)
{
  for (int i = 0; i < (int)a.size(); ++i)
    if (a[i] >= 'A' && a[i] <= 'Z')
      a[i] += 'a' - 'A';
  return a;
}

bool prime(ll a)
{
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

void FastIO()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
}

void solve()
{
  // 1 4 2 5 3 == [1, 2, 3] + [4, 5] (alternate)
  // 1 4 2 5 3 6 == [1, 2, 3] + [4, 5, 6] (alternate)
  // 1, 5, 2, 6, 3, 7, 4 === [1, 2, 3, 4] + [5, 6, 7] (alternate)
  // So, [1 to (n // 2)] + [(n // 2) + 1 to n] (alternate)

  // first, second last, second, third last, thrid, fourth last, fourth, ...
  // 1, (n - 1), 2, (n - 2), 3, (n - 3), ... till mid

  // 3 1 4 2
  
  int n;
  cin >> n;

  if(n <= 3) {
    if(n == 1) {
      cout << "1";
      return;
    }
    cout << "NO SOLUTION";
    return;
  } else if(n == 4) {
    cout << "3 1 4 2";
    return;
  }


  // ceil(x) = (x + 1) / 2 for integers
  // floort(x) = x / 2 for integers

  int mid = (n + 1) / 2;
  int i = 1, j = mid + 1;

  for(; i <= ((n + 1) / 2) && j <= n; ++i, ++j) {
    cout << i << " " << j << " ";
  }

  if(n % 2 == 1) {
    cout << mid;
  }

  return;
}

int main()
{
  FastIO();
  solve();
}