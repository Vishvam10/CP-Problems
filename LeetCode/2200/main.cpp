class Solution {
public:
    int minBitFlips(int start, int goal) {
        
        int res = start ^ goal;
        int ans = 0;

        while(res) {
            int lsb = res & 1;
            if(lsb == 1) {
                ans++;
            }
            // Remove the last bit
            res >>= 1;
            cout << endl;
        }
        
        return ans;

    }
};