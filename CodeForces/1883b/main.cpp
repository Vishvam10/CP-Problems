#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void solve(){
	int n, m, c = 0;
	string s;
	cin >> n >> m >> s;

	int mp[26] = {0};

	for(int i = 0; i < s.size(); i++){
		mp[s[i]-'a']++;
	}

    for(int i = 0; i < 26; i++){
		if(mp[i] % 2 == 1){
			c++;
		}
	}
	if(c - m > 1){
		cout << "NO\n";
	}
	else {
		cout << "YES\n";
	}
    return;
}

int main() {
    int n;
    cin >> n;

    while(n--) {
        solve();
    }

    return 0;
}




