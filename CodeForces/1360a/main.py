def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))


def solve() :
    [a, b] = inlt()
    print(min(max(2 * a, b), max(a, 2 * b)) ** 2)


t = inp()

for _ in range(t) :
    solve()
