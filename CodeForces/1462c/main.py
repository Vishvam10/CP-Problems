def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))


def solve() :

    n = inp()

    if(n > 45) :
        print("-1")
        return
    
    if(n >= 1 and n <= 9) :
        print(n)
        return
    
    used = [False] * 9
    ans = []

    for i in range(9, 0, -1) :
        temp = n - i
        if(not used[i-1] and temp >= 0) :
            n -= i
            ans.append(str(i))
            used[i-1] = True
   
    ans.sort()
    ans = int(''.join(ans))
    print(ans)
    return

t = inp()

for _ in range(t) :
    solve()
