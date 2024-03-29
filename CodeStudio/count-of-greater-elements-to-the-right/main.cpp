vector<int> countGreater(vector<int> &arr, vector<int> &query) {

  vector<int> ans;
  for (auto i : query) {
    int c = 0;
    for (int j = i + 1; j < arr.size(); j++) {
      if (arr[j] > arr[i]) {
        c++;
      }
    }
    ans.emplace_back(c);
  }
  return ans;
}