#include <iostream>

int main() {

    int a, b;
    std::cin >> a >> b;

    std::cout << std::min(a, b) << " " << (std::max(a, b) - std::min(a, b)) / 2<< std::endl;

    return 0;
}