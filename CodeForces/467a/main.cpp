#include <iostream>

int main() {

  int n;
  int ans = 0;
  std::cin >> n;

  for (int i = 0; i < n; i++) {
    int a, b;
    std::cin >> a;
    std::cin >> b;
    if (b - a >= 2) {
      ans++;
    }
  }
  std::cout << ans << std::endl;
  return 0;
}
