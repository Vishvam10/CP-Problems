#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

int gcd(int a, int b) {
    if(a == 0) {
        return b;
    }
    return gcd(b % a, a);
}

void solve() {

    int n, ans = 0;
    vector<int> arr;
    vector<int> temp;

    cin >> n;

    for(int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if(x % 2 == 0) {
            arr.emplace_back(x);
        } else {
            temp.emplace_back(x);
        }
    }

    for(int i = 0; i < temp.size(); i++) {
        arr.emplace_back(temp[i]);
    }

    for(int i = 0; i < n; i++) {
        for(int j = i+1; j < n; j++) {
            if(gcd(arr[i], 2 * arr[j]) > 1) {
                ans++;
            }
        }
    }

    cout << ans << "\n";

}

int main() {
    int t;
    cin >> t;
    while(t--) {
        solve();
    }
}