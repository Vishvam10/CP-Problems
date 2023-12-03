#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {

    string s;
    cin >> s;
    bool flag = false;

    for(int i = 0; i < s.length(); i++) {
        if(s[i] == 'W' && s[i + 1] == 'U' && s[i + 2] == 'B') {
            i += 2;
            if(flag) {
                cout << " ";
            }
            flag = false;
            continue;
        } else {
            flag = true;
            cout << s[i];
        }
    }

    return 0;
}