def inp():
    return(int(input()))

def inlt():
    return(list(map(int,input().split())))

def insr():
    return(input().strip())

def solve() :
    k = inp()
    arr = inlt()

    if(k == 0) :
        print('0')
        return

    arr.sort(reverse=True)
    s = 0

    for (i, x) in enumerate(arr) :
        s += x
        if(s >= k) :
            print(i + 1)
            return

    print('-1')
    return




solve()
