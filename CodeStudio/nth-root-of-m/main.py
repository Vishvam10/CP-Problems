def NthRoot(n: int, m: int) -> int:
    low, high = 0, m
    while(low <= high) :
        mid = low + (high - low) // 2
        val = mid ** n
        if(val == m) :
            return mid
        if(val > m) :
            high = mid - 1
        else :
            low = mid + 1
    
    return -1