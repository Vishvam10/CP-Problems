def unique(n):
    mp = {}
    while (n):
        dig = n % 10
        if (dig in mp):
            return False
        else:
            mp[dig] = True
        n //= 10

    return True


def solve():
    s = int(input().strip())
    flag = True
    while (flag):

        s += 1
        if (unique(s)):
            print(s)
            flag = False

    return -1


solve()
