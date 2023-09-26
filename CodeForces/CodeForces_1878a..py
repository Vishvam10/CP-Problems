def inp():
    return(int(input()))

def inlt():
    return(list(map(int,input().split())))

def insr():
    return(input().strip())

def solve() :
    [n, k] = inlt()
    arr = inlt()
    
    for i in range(n) :
        for j in range(i, n) :
            c = 0
            size = j - i
            for l in range(i, j+1) :
                if(arr[l] == k) :
                    c += 1
            # print('k, c, size : ', k, c, size)
            if(c > size // 2) :
                print("YES")
                return
    print("NO")
    return
                    
            
t = inp()

for _ in range(t) :
    solve()