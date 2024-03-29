class Solution {
public:
  vector<int> sortArrayByParity(vector<int> &arr) {
    // sort(arr.begin(), arr.end(), [](int a, int b) -> bool {
    //     return (a & 1) < (b & 1);
    // });

    int left = 0, right = arr.size() - 1;

    while (left <= right) {
      if (arr[left] % 2 > arr[right] % 2) {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
      }
      if (arr[left] % 2 == 0) {
        left++;
      }
      if (arr[right] % 2 == 1) {
        right--;
      }
    }

    return arr;
  }
};