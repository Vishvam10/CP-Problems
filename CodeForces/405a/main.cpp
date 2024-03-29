#include <algorithm>
#include <iostream>

int main() {

  int n;
  std::cin >> n;
  int arr[n];

  for (int i = 0; i < n; i++) {
    int a;
    std::cin >> a;
    arr[i] = a;
  }

  std::sort(arr, arr + n);

  for (int i = 0; i < n; i++) {
    std::cout << arr[i] << " ";
  }

  return 0;
}
