class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mp = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6':
              'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def helper(ind, pref, acc):

            if (len(pref) == len(digits)):
                acc.append(pref[:])
                return

            for val in mp[digits[ind]]:
                # Set the state
                pref.append(val)

                # Goto next state
                helper(ind + 1, pref, acc)

                # Reset the state
                pref.pop()

            return acc

        if (len(digits) <= 0):
            return []

        else:

            res = helper(0, [], [])
            ans = []

            for x in res:
                ans.append(''.join(x))

            return ans
