def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    return (input().strip())


s = insr()
a, b = 0, 0

for ch in s:
    if (ch.isupper()):
        a += 1
    else:
        b += 1

if (a > b):
    print(s.upper())
else:
    print(s.lower())
