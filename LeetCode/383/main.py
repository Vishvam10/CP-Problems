class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rm = collections.Counter(ransomNote)
        mg = collections.Counter(magazine)

        for k, v in rm.items():
            if k not in mg or mg[k] < v:
                return False

        return True
