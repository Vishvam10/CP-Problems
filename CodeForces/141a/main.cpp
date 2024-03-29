#include <bits/stdc++.h>
#include <iostream>
#include <string>

int main() {

  std::string a, b, c;
  std::cin >> a >> b >> c;

  std::string temp;
  temp = a + b;

  if (temp.length() > c.length()) {
    std::cout << "NO" << std::endl;
    return 0;
  }

  sort(temp.begin(), temp.end());
  sort(c.begin(), c.end());

  if (temp == c) {
    std::cout << "YES" << std::endl;
  } else {
    std::cout << "NO" << std::endl;
  }

  return 0;
}