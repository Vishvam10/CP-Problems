class Solution {
public:
    int nthUglyNumber(int n) {
        if(n == 1) {
            return 1;
        }
        int p1 = 0, p2 = 0, p3 = 0;
        vector<int> res(n, 0);
        res[0] = 1;

        // 3 pointers are updated on the res array as 
        // we want the last pos : the last element where 
        // that factor was used)
        for(int i = 1; i < n; i++) {
            int t1 = 2 * res[p1];
            int t2 = 3 * res[p2];
            int t3 = 5 * res[p3];
            
            int t4 = min({t1, t2, t3});
            if(t4 == t1) {
                p1++;
            } 
            if(t4 == t2) {
                p2++;
            } 
            if(t4 == t3) {
                p3++;
            }

            res[i] = t4;
        }
        
        return res[n-1];
    }
};