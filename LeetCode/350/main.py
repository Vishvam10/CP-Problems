class Solution:
    def intersect(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        arr1.sort()
        arr2.sort()
        i, j = 0, 0
        
        while(i < len(arr1) and j < len(arr2)) :
            if(arr1[i] > arr2[j]) :
                j += 1
            elif(arr1[i] < arr2[j]) :
                i += 1
            else :
                ans.append(arr1[i])
                i += 1
                j += 1
                
        return ans