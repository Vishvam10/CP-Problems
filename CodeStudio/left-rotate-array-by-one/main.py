import copy


def rotateArray(arr: [], n: int) -> []:

    cpy = copy.deepcopy(arr)
    k = 1
    for i in range(n):
        arr[(i-k) % n] = cpy[i]

    return arr
