class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        
        n = len(arr)

        if(n <= 2) :
            return n

        k, c = 1, 0

        for i in range(1, n) :
            if(arr[i] == arr[i-1]) :
                c += 1
            else :
                c = 0
    
            if(c < 2) :
                arr[k] = arr[i]
                k += 1

        return k