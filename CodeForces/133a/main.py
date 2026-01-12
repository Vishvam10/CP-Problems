def insr():
    return input().strip()


def solve():
    s = insr()

    for ch in s:
        if ch == "H" or ch == "Q" or ch == "9":
            print("YES")
            return
    print("NO")
    return


solve()
