class Solution:
    def checkValidString(self, s: str) -> bool:
        ls, rs, ss = 0, 0, 0
        for ch in s:
            if (ch == '('):
                ls += 1
            elif (ch == ')'):
                rs += 1
            else:
                ss += 1
        # print('difference : ', rs - ls, ' wildcard : ', ss)
        diff = abs(rs - ls)
        if (ss >= diff):
            return True
        return False
