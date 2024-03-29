class Solution {
public:
  int check(int n) {
    int c = 0, s = 0;
    for (int i = 1; i * i <= n; i++) {
      if (n % i == 0) {
        if (n / i == i) {
          return 0;
        }
        c += 2;
        s += i;
        s += (n / i);
      }
    }
    return c == 4 ? s : 0;
  }

  int sumFourDivisors(vector<int> &arr) {
    int n = arr.size();
    int ans = 0;

    for (int i = 0; i < n; i++) {
      ans += check(arr[i]);
    }

    return ans;
  }
};