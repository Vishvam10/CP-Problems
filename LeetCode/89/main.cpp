class Solution {
public:
  vector<int> ans;
  ;

  void solve(bitset<32> &bs, int pos) {
    if (pos == 0) {
      ans.emplace_back(bs.to_ulong());
      return;
    }

    solve(bs, pos - 1);
    bs.flip(pos - 1);
    solve(bs, pos - 1);
  }

  vector<int> grayCode(int n) {

    bitset<32> bs;
    solve(bs, n);

    return ans;
  }
};