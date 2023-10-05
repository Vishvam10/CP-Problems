def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    return(input().strip())

def solve() :
    # Construction : have all the even bags first and then the odd ones
    n = inp()
    arr = inlt()
    even = 0
    odd = 0
    for x in arr :
        if(x % 2 == 0) :
            even += x
        else :
            odd += x
    
    if(even > odd) :        
        print("YES")
        return
    
    print("NO")
    return
   
t = inp()

for _ in range(t) :
    solve()