import math

def insr():
    return(input().strip())

a = insr()
b = insr()
ans = ""

for i in range(len(a)) :
    if (
        (a[i] == "1" and b[i] == "1") or
        (a[i] == "0" and b[i] == "0") 
    ) :
        ans += "0"
    else :
        ans += "1"

print(ans)