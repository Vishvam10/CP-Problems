class Solution {
public:
  struct Node {
    int sum;
    int i;
    int j;

    Node(int _sum, int _i, int _j) : sum(_sum), i(_i), j(_j) {}

    bool operator<(const Node &node) const { return sum > node.sum; }
  };

  vector<vector<int>> kSmallestPairs(vector<int> &a, vector<int> &b, int k) {

    vector<vector<int>> ans;
    priority_queue<Node> h;

    int n = a.size();
    int m = b.size();

    for (int i = 0; i < n; i++) {
      h.push(Node(a[i] + b[0], i, 0));
    }

    while (!h.empty() && k > 0) {

      Node ele = h.top();
      h.pop();

      int i = ele.i;
      int j = ele.j;

      ans.push_back({a[i], b[j]});

      if (j + 1 != m) {
        h.push(Node(a[i] + b[j + 1], i, j + 1));
      }

      k--;
    }

    return ans;
  }
};