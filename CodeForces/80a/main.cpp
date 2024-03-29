#include <cmath>
#include <iostream>

bool isPrime(int n) {
  if (n <= 1) {
    return false;
  }

  for (int i = 2; i < int(pow(n, 0.5)) + 1; i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

int main() {

  int a, b;
  std::cin >> a >> b;

  if (isPrime(a) && isPrime(b)) {
    int c = 0;
    for (int x = a + 1; x <= b; x++) {
      if (isPrime(x))
        c++;
    }
    if (c == 1) {
      std::cout << "YES" << std::endl;
    } else {
      std::cout << "NO" << std::endl;
    }
  } else {
    std::cout << "NO" << std::endl;
  }

  return 0;
}