class Solution:
    def findSwapValues(self, a, n, b, m):
        # Your code goes here
        asum = sum(a)
        bsum = sum(b)
        if((asum - bsum) % 2 != 0):
            return -1
        else :
            target = (asum - bsum) // 2
       
        a.sort()
        b.sort()
        
        i, j = 0, 0
        while(i < n and j < m) :
            diff = a[i] - b[j]
            if(diff == target) :
                return 1
            elif(diff < target) :
                i += 1
            else :
                j += 1
        return -1
        
        # for x in a :
        #     for y in b :
        #         if(asum - x + y == bsum - y + x) :
        #             return 1
        
        # asum - bsum = 2x - 2y. 
        # Let target = 2x - 2y => 2x = target + 2y => Similar to 2Sum Problem
        
       