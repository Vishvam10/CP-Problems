def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def isPrime(x):
    if x <= 1:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True


a, b = inlt()
c = 0

if isPrime(a) and isPrime(b):
    for i in range(a + 1, b + 1):
        if isPrime(i):
            c += 1

    if c == 1:
        print("YES")
    else:
        print("NO")

else:
    print("NO")
