class Solution {
public:
    int findKthLargest(vector<int>& arr, int k) {
        map<int, int> mp;

        for(int&x : arr) {
            mp[x]++;
        }

        for (auto it = mp.rbegin(); it != mp.rend(); ++it) {
            k -= it->second;
            if (k <= 0) {
                return it->first;
            }
        }
        return -1;
     }
};