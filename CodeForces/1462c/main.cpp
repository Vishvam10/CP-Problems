#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;


void solve() {
    
    int n;
    cin >> n;

    if(n > 45) {
        cout << "-1\n";
        return;
    }
    
    if(n >= 1 && n <= 9) {
        cout << n << "\n";
        return;
    }
    
    bool used[9] = {false};
    vector<int> ans;

    for(int i = 9; i >= 1; i--) {
        int temp = n - i;
        if(!used[i-1] && temp >= 0) {
            n -= i;
            ans.emplace_back(i);
            used[i-1] = true;
        }
    }

    for(int i = ans.size() - 1; i >= 0; i--) {
        cout << ans[i] << "";
    }

    cout << "\n";
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
