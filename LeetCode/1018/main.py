"""
DIFFICULTY : easy
TAGS : array
"""


class Solution:
    # If X is the first i digits of the array as a binary number,
    # then 2X + A[i] is the first i+1 digits.

    # To add a digit at the end of a binary number :
    # new_number = old_number * 2 + digit
    #            = old_number >> 1 + digit

    # To solve the overflow problem :
    # (ab + c) % d === ((a % d)(b % d) + c % d) % d.
    # new_number % 5 = ((old_number % 5) * 2 + d) % 5

    def prefixesDivBy5(self, arr: List[int]) -> List[bool]:
        s = 0

        for i, x in enumerate(arr):
            s = (s * 2) % 5 + x
            if (s % 5 == 0):
                arr[i] = True
            else:
                arr[i] = False

        return arr
