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

void simulate(
    vector<int>

)
{

  // a chooses
}

void solve()
{
  int n, a, b;
  cin >> n >> a >> b;

  /*
    In each turn, we can have 3 outcomes :
      - a's score increases by x
      - b's score increases by y
      - no scores increase

    There can be atmost n turns as the total number of cards is n

    We can have ties and it's best to just remove (no. of ties) elements from
    the end

    n -= ties

    for turn in n :
      a += (1 if a's score is higher else 0)
      b += (1 if b's score is higher else 0)

    So, here we don't care about the "a chooses from 1..n, b chooses from 1..m"
    approach at all. All we care about it "how many turns did a win and how
    many turns did b win"

    Say n = 6 (whatever ties were there, we can just print it at the end as we
    don't care about them anyway)

    b = 5 (n - 1)

    a = 1, b = 2
    a = 2, b = 3
    a = 3, b = 4
    a = 4, b = 5
    a = 5, b = 6
    a = 6, b = 1 (lost)

    b = 4

    a = 1, b = 3
    a = 2, b = 4
    a = 3, b = 5
    a = 4, b = 6
    a = 5, b = 1 (lost)
    a = 6, b = 2 (lost)

    So, it's a cyclic pattern. We need to print a's moves first (which is just
    1 to n, then n + 1 to ties) and then b's moves (which is whatever 1 to n 
    offsetted by a, then n + 1 to ties)

  */

  // n = 4, a = 4, b = 1

  int ties = n - a - b;

  if(ties < 0) {
    cout << "NO" << "\n";
    return;
  }

  n -= ties;

  if(n < 0) {
    cout << "NO" << "\n";
    return;
  }

  // n >= 1 check is for cases like n = 10, a = b = 0 (like all ties only).
  // In that case, it's possible so not printing "NO"
  if((n >= 1) && (a == n || b == n)) {
    cout << "NO" << "\n";
    return;
  }

  cout << "YES" << "\n";

  // a's moves (here, I'm combining the ties, as it's just 1 to n + ties)
  for(int i = 1; i <= n + ties; ++i) {
    cout << i << " ";
  }

  cout << "\n";
  
  // b's moves
  for(int i = 1; i <= n; ++i) {
    
    int val = i + a;
    if(val > n) {
      // Start from 1 again
      val -= n;
    }

    cout << val << " ";
   
  }

  // b's ties (same as a's ties)
  for(int i = n + 1; i <= n + ties; ++i) {
    cout << i << " ";
  }

  cout << "\n";

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