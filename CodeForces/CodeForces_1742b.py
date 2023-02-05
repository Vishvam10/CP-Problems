def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))


def solve() :
    n = inp()
    a = inlt()
    a.sort()
    for i in range(1, n, 1) :
        if(a[i - 1] == a[i]) :
            print("NO")
            return
    print("YES")
    return


t = inp()

for _ in range(t) :
    solve()
