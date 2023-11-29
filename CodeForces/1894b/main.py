from collections import defaultdict

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    return(input().strip())

def solve() :
    n = inp()
    arr = inlt()

    mp = defaultdict(int)
    ans = [1] * n
    c = 1
    for (i, x) in enumerate(arr) :
        mp[x] += 1

        if(mp[x] == 2) :
            ans[i] = min(c + 1, 3)
            c += 1

    if(c > 2) :
        print(*ans)
    else :
        print('-1')

    return            


t = inp()

for _ in range(t) :
    solve()