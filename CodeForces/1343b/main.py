def solve():
    n = int(input())
    if (n == 2):
        print('NO')
        return

    check = (n // 2) % 2

    if (check == 0):
        print("YES")
        arr = []

        i, c, es = 0, 2, 0
        while (i < n//2):
            print(c, end=' ')
            c += 2
            i += 1
            es += c

        i, c, os = 0, 1, 0
        while (i < n//2 - 1):
            print(c, end=' ')
            c += 2
            i += 1
            os += c

        print(es - os - 2)
        return

    else:
        print('NO')
        return


t = int(input())

for i in range(t):
    solve()
