"""
DIFFICULTY : easy
TAGS : array, string, hash table, sorting
"""


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = []
        for i in range(len(names)):
            ans.append([heights[i], names[i]])
        ans = sorted(ans, reverse=True)
        return [name for height, name in ans]
