class Solution:
    def numberOfBeams(self, arr: List[str]) -> int:
        ans = 0
        row_counts = []
        
        for i in range(len(arr)) :
            row  = arr[i]
            count = 0
            for j in range(len(row)) :
                if(row[j] == "1") :
                    count += 1
            if(count != 0) :
                row_counts.append(count)
        
        for i in range(1, len(row_counts)) :
            ans += (row_counts[i-1] * row_counts[i])
        
        return ans
            
            