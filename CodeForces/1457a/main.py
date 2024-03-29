def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


n = inp()

for _ in range(n):

    x = inp()

    if (x & (x - 1)):
        print("YES")
    else:
        print("NO")
