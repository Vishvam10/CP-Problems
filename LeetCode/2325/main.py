"""
DIFFICULTY : easy
TAGS : string, hash table
"""


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mp = {" ": " "}
        i = 0
        ans = ""
        letters = "abcdefghijklmnopqrstuvwxyz"

        for ch in key:
            if ch not in mp:
                mp[ch] = letters[i]
                i += 1

        for ch in message:
            ans += mp[ch]

        return ans
