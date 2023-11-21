#include <iostream>

int main()
{

    int n;
    std::cin >> n;
    
    for(int i = 0; i < n; i++)
    {
        int a, b;
        std::cin >> a >> b;
        int c = std::min(std::max(2*a, b), std::max(a, 2*b));
        std::cout << c * c << std::endl;

    }

    return 0;
}