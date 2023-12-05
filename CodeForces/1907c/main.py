def inp():
    return(int(input()))

def inlt():
    return input().split()

def insr():
    return(input().strip())

def check(s) :
    for i in range(1, len(s)) :
        if(s[i-1] != s[i]) :
            return True
    return False

def solve() :
    n = inp()
    s = list(insr())
    mp = {}
    path = []

    def helper(s, ans) :
        key = ''.join(s)
        if(key in mp) :
            mp[key] = min(mp[key], ans)
            return mp[key]
        
        if(check(s)) :
            for i in range(1, len(s)) :
                if(s[i-1] != s[i]) :
                    temp = s[:i-1] + s[i+1:]

                    # Set the next state 
                    path.append(''.join(temp))

                    # Goto next state
                    ans = helper(temp, ans)

                    # Reset the state
                    path.pop()
        else :
            ans = min(ans, len(s))
            
        mp[key] = ans

        return ans

    res = helper(s, float('inf'))
    
    print(res)

    return

t = inp()

for _ in range(t) :
    solve()