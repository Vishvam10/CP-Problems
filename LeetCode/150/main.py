"""
DIFFICULTY : medium
TAGS : array, math, stack
"""


class Solution:
    # IMPORTANT NOTE :  "//" is not equal to
    # "int(float(a)/b)" i.e. truncate to zero

    # We don't check for stack underflow because the
    # question says that the solution always exists
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l + r)
                elif t == "-":
                    stack.append(l - r)
                elif t == "*":
                    stack.append(l * r)
                else:
                    stack.append(int(float(l) / r))
        return stack.pop()
