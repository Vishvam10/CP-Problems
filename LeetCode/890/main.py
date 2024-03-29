"""
DIFFICULTY : medium
TAGS : array, hash table, string
"""


class Solution:
    def getNumericPattern(self, w):
        arr = []
        mp = {}
        i = 0
        for i in range(len(w)):
            ch = w[i]
            if (ch in mp):
                arr.append(mp[ch])
            else:
                i += 1
                mp[ch] = i
                arr.append(mp[ch])

        return arr

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        num_pattern = self.getNumericPattern(pattern)
        for i in range(len(words)):
            num_word = self.getNumericPattern(words[i])
            if (num_word == num_pattern):
                ans.append(words[i])

        return ans
