def inp():
    return (int(input()))


def insr():
    return (input().strip())


n = inp()
s = insr()
count = 0
for i in range(1, n, 1):
    if (s[i-1] == s[i]):
        count += 1

print(count)
