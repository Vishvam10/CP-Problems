def inp():
    return(int(input()))
    
def insr():
    return(input().strip())


t = inp()

for _ in range(t) :
    s = insr()
    if(s in "codeforces") :
        print("YES")
    else :
        print("NO")