class Solution {
public:
  int removeDuplicates(vector<int> &arr) {
    int n = arr.size();
    if (n <= 2) {
      return n;
    }
    int c = 0, left = 1;

    for (int i = 1; i < n; i++) {
      if (arr[i - 1] == arr[i]) {
        c++;
      } else {
        c = 0;
      }
      if (c < 2) {
        arr[left] = arr[i];
        left++;
      }
    }

    return left;
  }
};