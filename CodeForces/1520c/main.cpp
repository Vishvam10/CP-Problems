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

// =============================================================================
// TYPEDEFS AND DEFINES
// =============================================================================

typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int uint64;

#define debug(...) debug_print(#__VA_ARGS__, __VA_ARGS__)
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795

// =============================================================================
// PRINTS AND UTILS
// =============================================================================

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

// =============================================================================
// NUMERICAL UTILS
// =============================================================================

int64 min(int64 a, int b)
{
  if (a < b)
    return a;
  return b;
}

int64 min(int a, int64 b)
{
  if (a < b)
    return a;
  return b;
}

int64 max(int64 a, int b)
{
  if (a > b)
    return a;
  return b;
}

int64 max(int a, int64 b)
{
  if (a > b)
    return a;
  return b;
}

int64 gcd(int64 a, int64 b)
{
  if (b == 0)
    return a;
  return gcd(b, a % b);
}

int64 lcm(int64 a, int64 b) { return a / gcd(a, b) * b; }

bool isPrime(int64 a)
{
  if (a == 1)
    return true;
  for (int i = 2; i <= round(sqrt(a)); ++i)
    if (a % i == 0)
      return false;
  return true;
}

// =============================================================================
// STRING UTILS
// =============================================================================

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

// =============================================================================
// INPUT UTILS
// =============================================================================

vector<int> split(const string &str, char delim = ' ')
{
  vector<int> result;
  stringstream ss(str);
  string token;

  while (getline(ss, token, delim))
  {
    if (!token.empty())
    {
      result.push_back(stoi(token));
    }
  }

  return result;
}

void FastIO()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
}

// =============================================================================
// MAIN
// =============================================================================

void solve()
{

  return;
}

int main()
{
  FastIO();
  int tc;
  cin >> tc;
  for (int t = 1; t <= tc; t++)
  {
    solve();
  }
}