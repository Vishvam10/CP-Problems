void immediateSmaller(vector<int> &arr) {
  for (int i = 1; i < arr.size(); i++) {
    arr[i - 1] = (arr[i] < arr[i - 1]) ? arr[i] : -1;
  }
}
