def inp():
    return(int(input()))

def inlt():
    return(list(map(int,input().split())))

def insr():
    return(input().strip())

def solve() :
    n = inp()
    s = insr()
    max_ = -1
    for i in range(n) :
        max_ = max(max_, ord(s[i]) - ord("a") + 1)
    
    print(max_)
    

t = inp()

for _ in range(t) :
    solve()