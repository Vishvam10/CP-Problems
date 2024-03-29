"""
DIFFICULTY : medium
TAGS : two pointers, string, trie, string matching
"""


class Solution:
    def camelMatch(self, arr: List[str], pat: str) -> List[bool]:
        def match(s1, s2):
            ptr1 = 0
            ptr2 = 0

            while (ptr1 < len(s1) and ptr2 < len(s2)):
                if (s1[ptr1] == s2[ptr2]):
                    ptr1 += 1
                    ptr2 += 1
                else:
                    if (s1[ptr1].isupper()):
                        return False
                    ptr1 += 1

            if (ptr2 == len(s2)):
                while (ptr1 < len(s1)):
                    if (s1[ptr1].isupper()):
                        return False
                    ptr1 += 1
                return True

            return False

        ans = []
        for word in arr:
            ans.append(match(word, pat))

        return ans
