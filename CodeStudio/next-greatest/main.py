def nextGreater(s):
    arr = list(s)
    n = len(arr)

    ind = -1

    for i in range(n-2, -1, -1) :
        if(arr[i] < arr[i+1]) :
            ind = i
            break
    
    if(ind == -1) :
        return '-1'

    
    for i in range(n-1, ind-1, -1) :
        if(arr[i] > arr[ind]) :
            break
        
    arr[i], arr[ind] = arr[ind], arr[i]

    # 534976 => 534679 not 536974
    arr[ind+1:] = reversed(arr[ind+1:])

    return ''.join(arr)

