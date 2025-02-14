"""
DIFFICULTY : easy
TAGS : string, string matching
"""


class Solution:
    # IDEA : The maximum length of a "repeated" substring that
    #        you could get from a string would be half it's length
    #        For example, s = "abcdabcd", "abcd" of len = 4,
    #        is the repeated substring. You cannot have a
    #        substring >(len(s)/2), that can be repeated.

    #        - So, when ss = s + s , we will have atleast 4 parts of
    #        "repeated substring" in ss.

    #        - With (s+s)[1:-1], we are removing 1st char and last char
    #        => Out of 4 parts of repeated substring, 2 part will be gone
    #        (they will no longer have the same substring).

    #        - ss.find(s) != -1, means that we still we have 2 parts out
    #        of which we can make s. And that's how ss should have s,
    #        if s has repeated substring.

    def repeatedSubstringPattern(self, s: str) -> bool:
        if (s is None):
            return False
        s1 = (s+s)[1:-1]
        return s1.find(s) != -1
