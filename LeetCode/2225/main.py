"""
DIFFICULTY : medium
TAGS : array, hash table, sorting, counting
"""
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers, table = [], [], {}
        for winner, loser in matches:
            # map.get(key, 0) returns map[key] 
            # if key exists and 0 if it does not.
            
            # table[winner] += 0
            table[winner] = table.get(winner, 0) 
            
            # table[loser] += 1
            table[loser] = table.get(loser, 0) + 1
            
        for k, v in table.items():
            if v == 0:
                winners.append(k) 
            if v == 1:
                losers.append(k) 
                
        return [sorted(winners), sorted(losers)]
        