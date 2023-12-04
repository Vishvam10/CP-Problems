def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    return(input().strip())

def solve() :
    n = inp()
    arr = inlt()

    pref = [0] * (n + 1)

    for i in range(n) :
        pref[i + 1] = pref[i] + arr[i]
    
    ans = 0

    for k in range(1, n + 1) :
        mx = -1
        mn = float("inf")
        if(n % k == 0) :
            for i in range(k, n + 1, k) :
                s = pref[i] - pref[i-k]
                mx = max(mx, s)
                mn = min(mn, s)

        ans = max(ans, mx - mn)
    
    print(ans)
    return
    

t = inp()

for _ in range(t) :
    solve()