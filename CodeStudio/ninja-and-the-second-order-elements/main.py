def getSecondOrderElements(n: int, a: [int]) -> [int]:
    m1 = float("-inf")
    m2 = float("inf")

    for i in range(n):
        if a[i] > m1:
            m1 = a[i]
        if a[i] < m2:
            m2 = a[i]

    ans1 = float("-inf")
    ans2 = float("inf")

    for i in range(n):
        if a[i] < m1:
            ans1 = max(ans1, a[i])
        if a[i] > m2:
            ans2 = min(ans2, a[i])

    return [ans1, ans2]
