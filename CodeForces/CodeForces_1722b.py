def inp():
    return(int(input()))

def inlt():
    return(list(map(int,input().split())))

def insr():
    return(input().strip())

def solve() :
    n = inp()
    s1 = insr().replace("B", "G")
    s2 = insr().replace("B", "G")

    print("YES" if s1 == s2 else "NO")


t = inp()

for _ in range(t) :
    solve()