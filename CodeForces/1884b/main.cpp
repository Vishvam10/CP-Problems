#include <iostream>
#include <set>

using namespace std;

typedef long long ll;
typedef long double ld;


void solve() {
    ll n;
    string arr;
    cin >> n >> arr;

    set<ll> mp;

    for(ll i = n - 1; i >= 0; i--) {
        if(arr[i] == '0') {
            mp.insert(-i);
        }
    }

    ll ans = 0;

    for(ll i = n - 1; i >= 0; i--) {
        if(mp.size() == 0) {
            cout << "-1 ";
        } else {
            ll ind = *mp.begin();
            ans += (i + ind);
            mp.erase(ind);
            cout << ans << " ";
        }
    }

    cout << "\n";

}

int main() 
{

    int t;
    cin >> t;

    while(t--) {
        solve();
    }
    

    return 0;
}
