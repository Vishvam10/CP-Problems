class Solution:
    def subsetsWithDup(self, arr: List[int]) -> List[List[int]]:
        def generate(arr, start, pref, acc):
            acc.append(pref)

            for i in range(start, len(arr)):
                if i > start and arr[i] == arr[i - 1]:
                    continue
                temp = pref + [arr[i]]
                generate(arr, i + 1, temp, acc)

            return acc

        arr.sort()  # To reduce the number of recursive calls
        ans = generate(arr, 0, [], [])

        return ans
