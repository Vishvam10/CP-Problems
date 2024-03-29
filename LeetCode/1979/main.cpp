int gcd(int a, int b) {
  if (a == 0) {
    return b;
  }
  return gcd(b % a, a);
}

class Solution {
public:
  int findGCD(vector<int> &arr) {
    int maxi = *max_element(arr.begin(), arr.end());
    int mini = *min_element(arr.begin(), arr.end());

    return gcd(maxi, mini);
  }
};