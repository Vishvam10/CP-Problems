def maximumAbsSum(arr, n):
    start, end, res = 0, 0, 0
    negIndex, posIndex = 0, 0
    curNeg, curPos = 0, 0

    for i in range(n):
        if arr[i][1] < 0:
            if abs(arr[i][1] + curNeg) > res:
                res = abs(arr[i][1] + curNeg)
                start = negIndex
                end = i
        else:
            if abs(arr[i][1] + curPos) > res:
                res = abs(arr[i][1] + curPos)
                start = posIndex
                end = i

        if curNeg + arr[i][1] > 0:
            curNeg = 0
            negIndex = i + 1
        else:
            curNeg -= arr[i][1]

        if curPos + arr[i][1] < 0:
            curPos = 0
            posIndex = i + 1
        else:
            curPos += arr[i][1]

    for i in range(start, end + 1):
        print(arr[i][0], end=" ")

    return


arr = [
    ["sample", 4],
    ["s", -3],
    ["asdf", 2],
    ["ds23", 3],
    ["skdf", 12],
    ["skdf123", 4],
    ["skdf534", 23],
    ["skdf53454", -29],
]
N = len(arr)

maximumAbsSum(arr, N)
