
#include <bits/stdc++.h>
#include <vector>

using namespace std;

#define ll long long
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vi vector<int>
#define vc vector<char>
#define vll vector<long long>
#define mpii map<int, int>
#define mpib map<int, bool>
#define umpii unordered_map<int, int>
#define umpib unordered_map<int, bool>
#define si set<int>
#define sc set<char>


template <class T>
void print_v(vector<T> &v)
{
    cout << "\n";
    for (auto x : v) {
        cout << x << " ";
    }
    cout << "\n";
}

char getRandomLetter()
{
    int random = rand() % 52; // Generate a random number in the range 0 to 51

    if (random < 26) {
        // Uppercase letter ('A' to 'Z')
        return ('A' + random);
    } else {
        // Lowercase letter ('a' to 'z')
        return ('a' + (random - 26));
    }
}

int main() {

    int n = 10;
    vi arr(n, 0);
    srand((unsigned) time(NULL));

    // cout << "letter : " << getRandomLetter();

    for(int i = 0; i < n; i++) {
        int num = rand() % n;
        arr[i] = num;
    }

    print_v(arr);

    return 0;
}