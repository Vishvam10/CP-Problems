def sortedArray(a: [int], b: [int]) -> [int]:
    n = len(a)
    m = len(b)
    ans = []

    p1 = p2 = 0

    # Merge 2 sorted array but add unique
    while(p1 < n and p2 < m) :
        if(a[p1] <= b[p2]) :
            # Add unique
            if(len(ans) == 0 or ans[-1] != a[p1]) :
                ans.append(a[p1])
            p1 += 1
        elif(a[p1] > b[p2]) :
            # Add unique
            if(len(ans) == 0 or ans[-1] != b[p2]) :
                ans.append(b[p2])
            p2 += 1
    
    while(p1 < n) :
        if(ans[-1] < a[p1]) :
            ans.append(a[p1])
        p1 += 1
    
    while(p2 < m) :
        if(ans[-1] < b[p2]) :
            ans.append(b[p2])
        p2 += 1

    return ans