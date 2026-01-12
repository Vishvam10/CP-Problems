def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    return input().strip()


a, b = inlt()

print(min(a, b), (max(a, b) - min(a, b)) // 2)
