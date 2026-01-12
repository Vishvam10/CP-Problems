class Solution:
    def reverseVowels(self, s: str) -> str:
        temp = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                temp.append(s[i])
                s[i] = "####"

        temp = temp[::-1]
        ptr = 0

        for i in range(len(s)):
            if s[i] == "####" and ptr < len(temp):
                s[i] = temp[ptr]
                ptr += 1

        return "".join(s)
