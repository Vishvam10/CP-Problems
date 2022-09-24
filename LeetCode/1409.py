"""
DIFFICULTY : medium
TAGS : array, binary indexed tree, simulation
"""
class Solution:    
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i+1 for i in range(m)]
        ans = []
        
        for i in range(len(queries)):
            ind = p.index(queries[i])
            p.pop(ind) 
            p.insert(0, queries[i])
            ans.append(ind)
            
        return ans