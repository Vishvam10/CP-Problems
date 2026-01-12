class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, a, b, n):
        # return: True or False
        mp = {}
        for x in a:
            if x in mp.keys():
                mp[x] += 1
            else:
                mp[x] = 1

        for x in b:
            if x not in mp.keys():
                return False
            else:
                mp[x] -= 1

        for v in mp.values():
            if v < 0:
                return False

        return True
