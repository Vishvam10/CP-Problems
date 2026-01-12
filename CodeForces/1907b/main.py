def inp():
    return int(input())


def inlt():
    return input().split()


def insr():
    return input().strip()


def solve():
    s = list(insr())
    lmp = []
    ump = []

    for i, ch in enumerate(s):
        if ch not in "bB":
            if ch.isupper():
                ump.append(i)
            else:
                lmp.append(i)
        else:
            if ch == "B":
                if len(ump) > 0:
                    s[ump[-1]] = ""
                    ump.pop()
                s[i] = ""
            elif ch == "b":
                if len(lmp) > 0:
                    s[lmp[-1]] = ""
                    lmp.pop()
                s[i] = ""

    print("".join(s))

    return


t = inp()

for _ in range(t):
    solve()
