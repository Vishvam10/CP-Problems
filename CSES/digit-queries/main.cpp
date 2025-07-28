#include <iostream>  // for cin, cout
#include <vector>    // for vector
#include <algorithm> // for max, min, sort, etc.
#include <numeric>   // for reduce
#include <map>       // for map
#include <set>       // for set
#include <cmath>     // for sqrt, round
#include <string>    // for string operations
#include <limits>    // for numeric_limits if needed
#include <sstream>   // for getline
#include <climits>   // for LLONG_MAX

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
  for (auto x : v)
  {
    cout << x << " ";
  }
}

template <class T>
void print_v2d(vector<vector<T>> &v)
{
  for (auto x : v)
  {
    for (auto y : x)
    {
      cout << y << " ";
    }
    cout << "\n";
  }
}

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

vector<int> split(const string& str, char delim = ' ') 
{
  vector<int> result;
  stringstream ss(str);
  string token;

  while (getline(ss, token, delim)) {
    if (!token.empty()) {
      result.push_back(stoi(token));
    }
  }

  return result;
}

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

int64 xpow(int64 x, uint64 y){
  int64 res = 1;
  while(y > 0) {
    if (y & 1) res = (res * x); y = y >> 1; x = (x * x);
  }
  return res;
}

void solve()
{

  // 1 2 3 .. 9 : (9 - 1 + 1) = 9 one digit = 9
  // 10 11 12 ... 99 : (99 - 10 + 1) = 90 two digit = 180
  // 100 101 102 ... 999 : (999 - 100 + 1) = 900 three digit = 2700
  // 1000 1001 1002 ... 9999 : (9999 - 1000 + 1) : 9000 four digit

  // 1  01112

  // Say q = 14, subtract 9 because it doesn't belong in that range := 5
  // Skip 5 / 2 = 2 and add (5 % 2) to it => digit = 1

  int64 n;
  cin >> n;

  // Number of digits and consequently, the counter (l)
  int num_digits = 1;

  while(n > xpow(9, num_digits)) {
    int64 cut =  (9 * xpow(10, num_digits - 1) * (num_digits));
    if (cut >= n) {
      break;
    } else {
      n -= cut;
    }
    num_digits++;
  }

  // The number is offsetted by 1 to the left
  n--;

  int64 start_num = xpow(10, num_digits - 1);

  int64 skip_digits = n / num_digits;
  int64 actual_num = start_num + skip_digits;

  // We could just return to_string(actual_ans)[n % num_digits] but if we want
  // to use loops to do it (using %), we need to convert the offset to 
  // "left-to-right" and digit extraction is "right-to-left"
  int64 offset = num_digits - (n % num_digits);
  int64 ans;

  while(actual_num > 0) {

    ans = actual_num % 10;
    actual_num /= 10;
    offset--;
    
    if(offset == 0) {
      cout << ans << "\n";
      return;
    }
  }

  return;
}

int main()
{
  FastIO();
  int tc;
  cin >> tc;
  for (int t = 1; t <= tc; t++) {
    solve();
  }
}