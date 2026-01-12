class Solution {
public:
  string minWindow(string s, string t) {
    int n = s.length(), m = t.length();
    if (m > n)
      return "";

    int freq[256] = {0};
    for (const char c : t)
      freq[c]++;

    int left = 0, cnt = 0;
    int startIndex = -1, minLen = INT_MAX;

    for (int right = 0; right < n; right++) {
      char rc = s[right];

      if (freq[rc] > 0)
        cnt++;
      freq[rc]--;

      while (cnt == m) {
        if (right - left + 1 < minLen) {
          minLen = right - left + 1;
          startIndex = left;
        }

        char lc = s[left];
        freq[lc]++;
        if (freq[lc] > 0)
          cnt--;
        left++;
      }
    }

    return startIndex == -1 ? "" : s.substr(startIndex, minLen);
  }
};