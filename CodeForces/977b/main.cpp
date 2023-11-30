#include <iostream>
#include <unordered_map>

using namespace std;

int main() 
{

    int n;
    string s;
    cin >> n >> s;

    int maxi = -1;
    string ans = "";
    unordered_map<string, int> mp;
    
    for(int i = 0; i < n - 1; i++) {
        string ss = s.substr(i, 2);
        mp[ss]++;
        if(mp[ss] >= maxi) {
            maxi = mp[ss];
            ans = ss;
        }
    }   

    cout << ans << "\n";

    return 0;
}



