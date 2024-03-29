def read(n: int, arr: [int], target: int) -> str:
    mp = {}
    for i in range(n):
        diff = target - arr[i]
        if (diff in mp and mp[diff] != i):
            return 'YES'
        mp[arr[i]] = i
    return 'NO'
