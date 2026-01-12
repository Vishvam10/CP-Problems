"""
DIFFICULTY : medium
TAGS : array, string, prefix sum
"""


class Solution:
    # IDEA :  Shifting adds up for every index

    #   Mark the beginning and ending of every range
    #   Instead of iterating through the range, we can
    #   add a +1 if we are moving forward in the beginning
    #   of the range and -1 in the end of the range. If we
    #   are moving backward, then -1 at the beginning
    #   and +1 at the end.

    #   Now do prefix sum on this.

    #   pre[i] is how many times we have to increase or
    #   decrease the s[i] char.

    #   NOTE : ord returns the unicode code of a character.
    #        a in unicode is 97 a simple %26 won't work
    #        So, it should be changed to : (ord(ch)-97)%26
    #        (which gives us a number between 0 and 25)
    #        Then add 97 to it to convert it back to
    #        unicode : ((ord(ch)-97)%26) + 97

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0 for _ in range(len(s) + 1)]

        # We take (end+1) as end is included
        for start, end, d in shifts:
            if d == 0:
                pre[start] -= 1
                pre[end + 1] += 1
            else:
                pre[start] += 1
                pre[end + 1] -= 1

        # for i in range(1, len(pre)) :
        #     pre[i] = pre[i] + pre[i-1]

        # We can compute the prefix sum on the fly

        cum_sum = 0
        for i in range(len(s)):
            # shifted_ch = (((ord(s[i]) + pre[i]) - 97) % 26) + 97

            cum_sum += pre[i]
            shifted_ch = (((ord(s[i]) + cum_sum) - 97) % 26) + 97

            s = s[:i] + chr(shifted_ch) + s[i + 1 :]

        return s
