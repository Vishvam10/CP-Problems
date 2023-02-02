def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))

n = inp()
arr = inlt()
ans = 0
curr = 0

for i in range(n) :
    if(arr[i] == -1) :
        if(curr > 0) :
            curr -= 1
        else :
            ans += 1
    else :
        curr += arr[i]

print(ans)