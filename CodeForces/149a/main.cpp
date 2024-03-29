#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int k;
  vector<int> arr;
  cin >> k;

  for (int i = 0; i < 12; i++) {
    int temp;
    cin >> temp;
    arr.push_back(temp);
  }
  int n = arr.size();
  int sum = 0;
  int month = 0;
  bool found = false;

  if (k == 0) {
    cout << 0 << endl;
    found = true;
  }

  sort(arr.begin(), arr.end());

  for (int i = n - 1; i >= 0 && !found; i--) {
    sum += arr[i];
    month++;
    if (sum >= k) {
      cout << month << endl;
      found = true;
      break;
    }
  }
  if (!found)
    cout << -1 << endl;
  return 0;
}