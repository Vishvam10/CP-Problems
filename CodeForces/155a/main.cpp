#include <iostream>
#include <stack>

int main() {

  int n, ans = 0;
  std::cin >> n;
  std::stack<int> max_till_now, min_till_now;

  for (int i = 0; i < n; i++) {
    int a;
    std::cin >> a;
    if (i == 0) {
      max_till_now.push(a);
      min_till_now.push(a);
    }
    if (a > max_till_now.top()) {
      ans++;
      max_till_now.push(a);
    } else if (a < min_till_now.top()) {
      ans++;
      min_till_now.push(a);
    }
  }

  std::cout << ans << std::endl;

  return 0;
}
