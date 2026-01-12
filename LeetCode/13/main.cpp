class Solution {
public:
  int romanToInt(string s) {

    int n = s.length();
    int i = 0, ans = 0;

    while (i < n) {
      char ch = s[i];
      char nxt = 0;
      if (i + 1 < n) {
        nxt = s[i + 1];
      }

      if (ch == 'I') {
        if (nxt == 'V') {
          ans += 4;
          i += 2;
        } else if (nxt == 'X') {
          ans += 9;
          i += 2;
        } else {
          ans += 1;
          i += 1;
        }
      } else if (ch == 'X') {
        if (nxt == 'L') {
          ans += 40;
          i += 2;
        } else if (nxt == 'C') {
          ans += 90;
          i += 2;
        } else {
          ans += 10;
          i += 1;
        }
      } else if (ch == 'C') {
        if (nxt == 'D') {
          ans += 400;
          i += 2;
        } else if (nxt == 'M') {
          ans += 900;
          i += 2;
        } else {
          ans += 100;
          i += 1;
        }
      } else if (ch == 'V') {
        ans += 5;
        i += 1;
      } else if (ch == 'L') {
        ans += 50;
        i += 1;
      } else if (ch == 'D') {
        ans += 500;
        i += 1;
      } else if (ch == 'M') {
        ans += 1000;
        i += 1;
      }
    }

    return ans;
  }
};
