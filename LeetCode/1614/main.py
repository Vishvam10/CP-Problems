class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
         c = 0
          ans = 0

           for i in range(n):
                ch = s[i]
                # print('ch, c, ans : ', ch, c, ans)
                if (ch == '('):
                    c += 1
                elif (ch == ')'):
                    ans = max(ans, c)
                    c -= 1

            return ans
