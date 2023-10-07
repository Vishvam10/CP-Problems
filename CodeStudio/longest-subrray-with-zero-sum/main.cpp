#include <bits/stdc++.h>

int LongestSubsetWithZeroSum(vector < int > arr) {
  int n = arr.size();
  int pref = 0, ans = 0;
  unordered_map<int, int> mp;
  
  for(int i=0; i<n; i++) {
    pref += arr[i];
    if(mp.find(pref) != mp.end()) {
      ans = max(ans, i-mp[pref]);
    } else {
      if(pref == 0) {
        ans = max(ans, i+1);
      } else {
        mp[pref] = i;
      }
    }
  }

  return ans;

}