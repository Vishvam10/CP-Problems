"""
DIFFICULTY : easy
TAGS : array, string, hash table, sorting
"""
class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        mp = {}
        ans = []
        for i in range(len(arr)) :
            word = "".join(sorted(arr[i]))
            if(word in mp) :
                mp[word].append(i)
            else :
                mp[word] = []
                mp[word].append(i)
        
        for k, v in mp.items() :
            temp = []
            for val in v :
                temp.append(arr[val])
            ans.append(temp)
        return ans