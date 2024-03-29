string nextGreater(string s) {

  // This is inplace

  int ind = -1;
  int n = s.length();
  string ans = "";

  for (int i = n - 2; i >= 0; i--) {
    if (s[i] - '0' < s[i + 1] - '0') {
      ind = i;
      break;
    }
  }

  if (ind == -1) {
    return "-1";
  }

  for (int i = n - 1; i > ind; i--) {
    if (s[i] - '0' > s[ind] - '0') {
      swap(s[i], s[ind]);
      break;
    }
  }

  reverse(s.begin() + ind + 1, s.end());

  return s;
}