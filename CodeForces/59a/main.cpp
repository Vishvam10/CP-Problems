#include <iostream>
#include <algorithm> 
#include <string>

int main()
{

    std::string s;
    std::cin >> s;

    int a = 0, b = 0;
    
    for(int i = 0; i < s.length(); i++) {
        if(std::isupper(s[i])) {
            a++;
        } else {
            b++;
        }
    }

    if(a > b) {
        std::transform(s.begin(), s.end(), s.begin(), ::toupper);
        std::cout << s << std::endl;
    } else {
        std::transform(s.begin(), s.end(), s.begin(), ::tolower);
        std::cout << s << std::endl;
    }
    

    return 0;
}