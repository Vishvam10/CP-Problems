"""
DIFFICULTY : easy
TAGS : two pointers, strings, greedy 
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check(s):
            n = len(s)
            left = 0
            right = n - 1

            while (left <= right):
                if (s[left] == s[right]):
                    left += 1
                    right -= 1
                else:
                    return False

            return True

        left = 0
        right = len(s) - 1
        count = 0
        while (left <= right):
            if (s[left] == s[right]):
                left += 1
                right -= 1
            else:
                if (count <= 1):
                    left_s = s[:left] + s[left+1:len(s)]
                    right_s = s[:right] + s[right+1:len(s)]
                    print(left, right, left_s, right_s)
                    if (check(left_s) or check(right_s)):
                        return True
                    else:
                        return False
                else:
                    return False
        return True
