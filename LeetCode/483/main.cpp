typedef unsigned long long ull;

class Solution {
public:
  string smallestGoodBase(string n) {
    ull tn = (ull)stoll(n);
    ull x = 1;
    for (int i = 62; i >= 1; i--) {
      if ((x << i) < tn) {
        ull cur = mysolve(tn, i);
        if (cur != 0)
          return to_string(cur);
      }
    }
    return to_string(tn - 1);
  }

  ull mysolve(ull n, int d) {
    double tn = (double)n;
    ull right = (ull)(pow(tn, 1.0 / d) + 1);
    ull left = 1;
    while (left <= right) {
      ull mid = left + (right - left) / 2;
      ull sum = 1, cur = 1;
      for (int i = 1; i <= d; i++) {
        cur *= mid;
        sum += cur;
      }
      if (sum == n)
        return mid;
      if (sum > n)
        right = mid - 1;
      else
        left = mid + 1;
    }
    return 0;
  }
};