def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    return(input().strip())

def solve() :
    n = inp()
    temp_a = 0
    temp_b = 0
    temp_c = 0
    for _ in range(n) :
        [a, b, c] = inlt()
        temp_a += a
        temp_b += b
        temp_c += c

    if(temp_a == 0 and temp_b == 0 and temp_c == 0) :
        print("YES")
    else :
        print("NO")
    return

solve()