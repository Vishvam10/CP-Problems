def insr():
    return(input().strip())

a = insr()
b = insr()

if(a == b[::-1]) :
    print("YES")
else :
    print("NO")
