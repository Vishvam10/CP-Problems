class Solution {
public:
    int singleNumber(vector<int>& arr) {
        int ans = 0;
        for(int i = 0; i < arr.size(); i++) {
            ans ^= arr[i];
        }
        return ans;
    }
};

/*

a XOR 0 = a
a XOR a = 0

*/