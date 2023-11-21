#include <iostream>

void solve() {
    int n;
    std::cin >> n;

    if((n / 2) % 2 == 1) {
        std::cout << "NO" << std::endl;
    } else {
        std::cout << "YES" << std::endl;
        
        int i = 0, c = 2, es = 0, os = 0;

        while(i < n/2)
        {
            std::cout << c << " ";
            c += 2;
            i += 1;
            es += c;
        }

        i = 0, c = 1;

        while(i < n/2 - 1)
        {
            std::cout << c << " ";
            c += 2;
            i += 1;
            os += c;
        }

        std::cout << es - os - 2 << std::endl;
    }

}

int main()
{
    int n;
    std::cin >> n;

    for(int i = 0; i < n; i++) {
        solve();
    }

    return 0;
}