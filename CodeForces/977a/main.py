def inlt():
    return list(map(int, input().split()))


[n, k] = inlt()
count = 0

for _ in range(k):
    rem = n % 10
    if rem != 0:
        n -= 1
    else:
        n //= 10

print(n)
