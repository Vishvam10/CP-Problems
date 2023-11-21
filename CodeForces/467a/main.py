def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    return(input().strip())

n = inp()
ans = 0
for i in range(n) :
    a, b = inlt()
    if b - a >= 2 :
        ans +=1
print(ans)