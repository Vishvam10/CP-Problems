def inp():
    return (int(input()))


def inlt():
    return input().split()


def insr():
    return (input().strip())


def solve():
    s = insr()
    r, c = s[0], int(s[1])
    ans = []

    # col
    for i in range(1, 9):
        if (i == c):
            continue
        ans.append(f'{r}{i}')

    # row
    for ch in 'abcdefgh':
        if (ch == r):
            continue
        ans.append(f'{ch}{str(c)}')

    for x in ans:
        print(x)

    return


t = inp()

for _ in range(t):
    solve()
