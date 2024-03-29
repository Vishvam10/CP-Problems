def inp():
    return (int(input()))


def insr():
    return (input().strip())


def solve():

    n = inp()
    temp = []
    i = 0
    while (n):
        dig = n % 10
        if 10**i * dig != 0:
            temp.append(10**i * dig)
        n //= 10
        i += 1

    print(len(temp))
    for x in temp[::-1]:
        print(x, end=" ")


t = inp()

for _ in range(t):
    solve()
