class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        def isPrefix(a, b) :
            for i in range(len(a)) :
                if(a[i] != b[i]) :
                    return False
            return True
        n = len(s)
        ans = 0
        for i in range(len(words)) :
            w = words[i]
            if(n >= len(w)) :
                if(isPrefix(w, s)) :
                    ans += 1
        return ans