def inp():
    return(int(input()))

def inlt():
    return input().split()

def insr():
    return(input().strip())

def solve() :
    s = insr()
    print(s.replace("WUB", " ").strip())
    return

solve()