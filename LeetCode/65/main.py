"""
DIFFICULTY : hard
TAGS : string
"""


class Solution:
    # IDEA :
    #   1. If char == + or char == -, then prev char (if there is) must be e
    #   2. . cannot appear twice or after e
    #   3. e cannot appear twice, and there must be at least one digit before and after e
    #   4. All other non-digit char is invalid

    # For a DFA based solution, refer :
    # https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA

    def isNumber(self, s: str) -> bool:
        seen_digit = seen_e = seen_dot = False

        s = s.strip()

        for i, ch in enumerate(s):
            if ch in "+-":
                if i > 0 and s[i - 1].lower() != "e":
                    return False
            elif ch == ".":
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif ch.lower() == "e":
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False
            elif ch in "0123456789":
                seen_digit = True
            else:
                return False

        return seen_digit
