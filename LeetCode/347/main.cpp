class Solution {
public:
  vector<int> topKFrequent(vector<int> &arr, int k) {

    int n = arr.size();
    vector<int> ans;
    unordered_map<int, int> mp;
    priority_queue<pair<int, int>, vector<pair<int, int>>> h;

    for (int i = 0; i < n; i++) {
      mp[arr[i]]++;
    }

    // when using pair, order is based on the first ele of heap
    // we want the order to be based on freq.
    // hence it->second goes first
    for (auto it = mp.begin(); it != mp.end(); it++) {
      h.push({it->second, it->first});
    }

    while (!h.empty() && k--) {
      ans.emplace_back(h.top().second);
      h.pop();
    }

    return ans;
  }
};