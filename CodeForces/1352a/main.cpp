#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> ans;
    int power = 1;
    while (n > 0) {
        if (n % 10 > 0) {
            ans.push_back((n % 10) * power);
        }
        n /= 10;
        power *= 10;
    }
    cout << ans.size() << endl;
    for (auto number : ans) cout << number << " ";
    cout << endl;

}

int main() {
    int n;
    cin >> n;

    while(n--) {
        solve();
    }

    return 0;
}




