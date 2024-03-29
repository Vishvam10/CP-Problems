int calculateMinPatforms(int arr[], int dep[], int n) {
  // Write your code here.
  sort(arr, arr + n);
  sort(dep, dep + n);

  int i = 1, j = 0, platforms = 1, ans = 1;

  while (i < n && j < n) {
    if (arr[i] < dep[j]) {
      platforms++;
      i++;
    } else {
      platforms--;
      j++;
    }
    ans = max(ans, platforms);
  }

  return ans;
}