#include <stack>
#include <unordered_map>

class Solution {
public:
  vector<int> nextGreaterElement(vector<int> &arr1, vector<int> &arr2) {
    vector<int> ans;
    stack<int> st;
    unordered_map<int, int> mp;
    int n = arr2.size();

    for (int i = n - 1; i >= 0; i--) {
      int ele = arr2[i];
      while (!st.empty() && st.top() < = ele) {
        st.pop();
      }
      int res = (st.empty()) ? -1 : st.top();

      // mp.insert({ele,res});
      mp[ele] = res;
      st.push(ele);
    }
    for (auto x : arr1) {
      ans.push_back(mp[x]);
    }
    return ans;
  }
};