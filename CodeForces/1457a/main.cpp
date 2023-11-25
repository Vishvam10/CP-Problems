#include <iostream>
#include <algorithm> 

typedef long long ll; 
typedef long double ld;

void solve() {
    ll n;
    std::cin >> n;
    if (n & (n - 1)) {
        std::cout << "YES\n";
    } else {
        std::cout << "NO\n";
    }
}

int main() 
{

    int n;
    std::cin >> n;
    
    for(int i = 0; i < n; i++) {
        solve();
    }

    return 0;
}
