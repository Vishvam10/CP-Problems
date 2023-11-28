#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;
typedef long double ld;


void solve() {
    ld a, b, c, c1, c2, c3;
    cin >> a >> b >> c;

    // a, b, c => (b - a) = (c - b) but it's not
    // so, either m*a or m*b or m*c :
    // 1. (b - ma) = (c - b) => 2b = ma + c => (2b - c) / a = m 
    // 2. (mb - a) = (c - mb) => 2mb = a + c => (a + c) / 2b = m
    // 3. (b - a) = (mc - b) => mc = 2b - a => (2b - a) / c = m

    c1 = (2*b - c) / a;
    c2 = (2*b - a) / c;
    c3 = (a + c) / (2*b);

    if(c1 > 0 && c1 == floor(c1)) {
        cout << "YES\n";
        return;
    }
    if(c2 > 0 && c2 == floor(c2)) {
        cout << "YES\n";
        return;
    }
    if(c3 > 0 && c3 == floor(c3)) {
        cout << "YES\n";
        return;
    }

    cout << "NO\n";
    return;
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
