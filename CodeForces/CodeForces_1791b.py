def inp():
    return(int(input()))
    
def insr():
    return(input().strip())

def solve() :
    n = inp()
    s = insr()
    x = 0
    y = 0
    for ch in s :
        if(ch == "L") :
            x -= 1
        if(ch == "R") :
            x += 1
        if(ch == "U") :
            y += 1
        if(ch == "D") :
            y -= 1

        if(x == 1 and y == 1) :
            print("YES")
            return

    print("NO")

t = inp()

for _ in range(t) :
    solve()