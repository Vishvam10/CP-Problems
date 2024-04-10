class Solution {
public:
  int removeDuplicates(vector<int> &arr) {
    int n = arr.size();
    int left = 0;

    for (int i = 1; i < n; i++) {
      if (arr[i] != arr[left]) {
        left++;
        arr[left] = arr[i];
      }
    }

    return left + 1;
  }
};