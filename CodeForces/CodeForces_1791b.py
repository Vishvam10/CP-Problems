def inp():
    return(int(input()))
    
def insr():
    return(input().strip())


t = inp()

for _ in range(t) :
    n = inp()
    s = insr()
    cur = [0, 0]
    flag = False
    for ch in s :
        if(ch == "L") :
            cur[0] -= 1
        elif(ch == "R") :
            cur[0] += 1
        elif(ch == "U") :
            cur[1] += 1
        elif(ch == "D") :
            cur[1] -= 1

        if(cur[0] == 1 and cur[1] == 1) :
            flag = True
            break
    if(flag) :
        print("Answer : ", "YES")
    else :
        print("Answer : ", "NO")