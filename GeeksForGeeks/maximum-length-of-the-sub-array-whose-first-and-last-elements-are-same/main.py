def max_length_subarray_whose_first_and_last_elements_are_same(arr, n):
    mp = {}  # can also use a character arr : chs = [0]*26 a
    max_len = -1
    ans = ""

    for i in range(n):
        if arr[i] not in mp:
            mp[arr[i]] = [i, -1]

    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]][1] = i

    for k, v in mp.items():
        if v[1] - v[0] + 1 > max_len:
            max_len = v[1] - v[0] + 1
            ans = k

    print("ans, length : ", ans, max_len)

    return ans


arr = ["a", "b", "c", "d", "a"]
# arr = ["g", "e", "e", "k", "s"]
n = len(arr)

max_length_subarray_whose_first_and_last_elements_are_same(arr, n)
