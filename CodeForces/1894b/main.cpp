#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

void solve() {
    int n;
    cin >> n;

    int a, c = 1;
    unordered_map<int, int> mp;
    vector<int> ans(n, 1);

    for(int i = 0; i < n; i++) {
        cin >> a;
        mp[a]++;
        if(mp[a] == 2) {
            ans[i] = min(c + 1, 3);
            c++;
        }
    }

    if(c > 2) {
        for(int i = 0; i < n; i++) {
            cout << ans[i] << " ";
        }
    } else {
        cout << "-1";
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