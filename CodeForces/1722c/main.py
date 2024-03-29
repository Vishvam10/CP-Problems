def inp():
    return (int(input()))


def inlt():
    return input().split()


def insr():
    return (input().strip())


def solve():
    n = inp()
    a1 = inlt()
    a2 = inlt()
    a3 = inlt()

    c1 = 0
    c2 = 0
    c3 = 0

    for x in a1:
        if (x in a2):
            if (x not in a3):
                c1 += 1
        elif (x in a3):
            if (x not in a2):
                c1 += 1
        else:
            c1 += 3

    for x in a2:
        if (x in a1):
            if (x not in a3):
                c2 += 1
        elif (x in a3):
            if (x not in a1):
                c2 += 1
        else:
            c2 += 3

    for x in a3:
        if (x in a2):
            if (x not in a1):
                c3 += 1
        elif (x in a1):
            if (x not in a2):
                c3 += 1
        else:
            c3 += 3

    print(c1, c2, c3)


t = inp()

for _ in range(t):
    solve()
