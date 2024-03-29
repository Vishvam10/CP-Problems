"""
DIFFICULTY : medium
TAGS : string, prefix sum
"""


class Solution:

    # penalty[i] = # Ns before i + # Ys after i

    def bestClosingTime(self, s: str) -> int:
        n = len(s)
        n_s = [0]*(n+1)  # n_s[i] = The no. of Ns before i
        y_s = [0]*(n+1)  # y_s[i] = The no.of Ys after i
        min_penalty = float("inf")
        min_ind = float("inf")

        temp = 0
        for i in range(n):
            ch = s[i]
            n_s[i] = temp
            if (ch == "N"):
                temp += 1

        n_s[n] = temp

        temp = 0
        for i in reversed(range(n)):
            ch = s[i]
            if (ch == "Y"):
                temp += 1
            y_s[i] = temp

        for i in range(n+1):
            penalty = n_s[i] + y_s[i]
            if (penalty < min_penalty):
                min_penalty = penalty
                min_ind = i

        return min_ind
