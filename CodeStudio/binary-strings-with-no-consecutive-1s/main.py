from typing import List


def generateString(n: int) -> List[str]:

    def solve(pref, n, acc):
        if (len(pref) == n):
            acc.append(pref)
            return acc

        if (len(pref) < n):

            if (pref == '' or pref[-1] == '0'):

                # Set the state
                temp = pref + '0'

                # Goto next state
                solve(temp, n, acc)

                # Set the state
                temp = pref + '1'

                # Goto next state
                solve(temp, n, acc)

            else:

                # Set the state
                temp = pref + '0'

                # Goto next state
                solve(temp, n, acc)

            return acc

        return acc

    ans = solve('', n, [])

    # print('ans : ', ans)

    return ans
