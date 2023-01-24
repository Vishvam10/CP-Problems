"""
DIFFICULTY : easy
TAGS : string, hash table, counting
"""
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        paragraph = paragraph.lower()
        count = 0
        ans = ""
        symbols = "!?',;."
        for sym in symbols:
            paragraph = paragraph.replace(sym, " ")
        
        all_words = paragraph.split()
        words = list(set(paragraph.split()))
        for word in words:
            if word not in banned:
                if all_words.count(word) > count:
                    count = all_words.count(word)
                    ans = word
        return ans