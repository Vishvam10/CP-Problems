class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n <= 0) {
            return false;
        }
        int mask = (n-1);
        int res = n & (n-1);
        if(res == 0) {
            return true;
        }
        return false;
    }
};