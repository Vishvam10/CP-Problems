class Solution {
public:
  int lastStoneWeight(vector<int> &arr) {

    int n = arr.size();
    priority_queue<int, vector<int>> h(arr.begin(), arr.end());

    while (h.size() > 1) {

      int a = h.top();
      h.pop();

      int b = h.top();
      h.pop();

      if (a != b) {
        h.push(a - b);
      }
    }

    return (h.size() == 0) ? 0 : h.top();
  }
};