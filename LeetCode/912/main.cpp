class Solution {
public:
  void merge(vector<int> &arr, int left, int mid, int right) {
    int i = left;
    int j = mid + 1;
    int k = 0;

    vector<int> temp(right - left + 1);

    while (i <= mid && j <= right) {
      if (arr[i] <= arr[j]) {
        temp[k++] = arr[i++];
      } else {
        temp[k++] = arr[j++];
      }
    }

    while (i <= mid) {
      temp[k++] = arr[i++];
    }

    while (j <= right) {
      temp[k++] = arr[j++];
    }

    // overwrite
    k = 0;

    for (int i = left; i <= right; i++) {
      arr[i] = temp[k++];
    }
  }

  void mergeSort(vector<int> &arr, int left, int right) {
    if (left >= right) {
      return;
    }

    int mid = left + (right - left) / 2;

    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);

    return;
  }

  vector<int> sortArray(vector<int> &arr) {

    mergeSort(arr, 0, arr.size() - 1);

    return arr;
  }
};