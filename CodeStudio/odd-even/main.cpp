string oddEven(int n) {
  int mask = 1;
  bool res = n & mask;
  if (res) {
    return "odd";
  }
  return "even";
}