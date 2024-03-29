def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def solve():
    a, b, c = inlt()

    # a, b, c => (b - a) = (c - b) but it's not
    # so, either m*a or m*b or m*c :
    # 1. (b - ma) = (c - b) => 2b = ma + c => (2b - c) / a = m
    # 2. (mb - a) = (c - mb) => 2mb = a + c => (a + c) / 2b = m
    # 3. (b - a) = (mc - b) => mc = 2b - a => (2b - a) / c = m

    c1 = (2*b - a) / c
    c2 = (2*b - c) / a
    c3 = (a + c) / (2*b)

    if (c1 > 0 and c1 % 1 == 0):
        print("YES")
        return

    if (c2 > 0 and c2 % 1 == 0):
        print("YES")
        return

    if (c3 > 0 and c3 % 1 == 0):
        print("YES")
        return

    print("NO")
    return


t = inp()

for _ in range(t):
    solve()
