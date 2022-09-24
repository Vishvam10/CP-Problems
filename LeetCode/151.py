"""
DIFFICULTY : medium
TAGS : string, two pointers
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed([x.strip() for x in s.split()]))