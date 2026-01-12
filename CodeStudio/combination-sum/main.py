from copy import copy  # Some issue with the driver code


def combSum(arr, target):
    arr.sort()

    def helper(arr, target, pref, acc):
        if target < 0:
            return
        if target == 0:
            acc.append(pref)

        for i in range(len(arr)):
            temp = pref + [arr[i]]
            helper(arr[i:], target - arr[i], temp, acc)

        return acc

    ans = helper(arr, target, [], [])
    return ans
