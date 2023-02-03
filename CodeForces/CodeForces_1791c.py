def inp():
    return(int(input()))
    
def insr():
    return(input().strip())

t = inp()

for _ in range(t) :
    n = inp()
    s = insr()

    left = 0
    right = n - 1
    ans = 0
    while(left <= right) :
        if((s[left] == "0" and s[right] == "1") or (s[left] == "1" and s[right] == "0")) :
            left += 1
            right -= 1
        else :
            break
        
    print(right - left + 1)