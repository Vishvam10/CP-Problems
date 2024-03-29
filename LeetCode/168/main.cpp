class Solution {
public:
  string convertToTitle(int n) {
    int rem = 0;
    string ans = "";

    while (n > 26) {
      n--;
      rem = n % 26;
      ans = char('A' + rem) + ans;
      n /= 26;
    }

    n--;
    ans = char('A' + n) + ans;

    return ans;
  }
};