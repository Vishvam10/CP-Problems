class Solution:
    def climbStairs(self, n: int) -> int:
        if(n <= 0) :
            return 0;
        if(n == 1) :
            return 1;
        if(n == 2) :
            return 2;
        fi, se, th = 2, 1, 0
        for i in range(2, n) :
            th = fi + se;
            se = fi;
            fi = th;
        return th;