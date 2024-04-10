class Solution {
public:
  int lengthOfLastWord(string s) {
    int n = s.length();
    int ptr = 0;
    for (int i = n - 1; i >= 0; i--) {
      if (s[i] == ' ') {
        if (ptr > 0) {
          return ptr;
        }
      } else {
        ptr++;
      }
    }
    return ptr;
  }
};