#include <iostream>
#include <vector>

using namespace std;

int main() {

    int n;
    cin >> n;
    vector<int> arr;

    for(int i = 0; i < n; i++) {
        int x;
        cin >> x;
        arr.emplace_back(x);
    }

    int ans = 0, c = 1;
    int prev = arr[0];

    for(int i = 1; i < n; i++) {
        if(arr[i] < prev) {
            ans = max(ans, c);
            c = 1;
        } else {
            c++;
        }
        prev = arr[i];
    }

    ans = max(ans, c);

    cout << ans << "\n";

    return 0;
}
