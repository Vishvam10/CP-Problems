def inp():
    return(int(input()))
def insr():
    return(input().strip())

def solve() :
    n = inp()
    s = insr().lower()
    ck = s[0]
    for i in range(1,n):
        if s[i]!=s[i-1]:
            ck+=s[i]
    if ck == "meow":
        print("YES")
    else:
        print("NO")

t = inp()

for _ in range(t) :
    solve()