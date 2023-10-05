'''    
    LOWER BOUND : smallest index i such that arr[i] >= x.
    
    
    For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such that the value 'arr[idx]' is not less than 'x'

    The lower bound is the smallest index, ind, where arr[ind] >= x. 
    
    IMP : But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.

'''

def lowerBound(arr: [int], n: int, x: int) -> int:
        
    left = 0
    right = n-1
    ans = 0

    while(left <= right) :
        mid = left + (right - left) // 2
        
        if(arr[mid] == x) :
            ans = mid
            right = mid - 1
        elif(arr[mid] < x) :
            left = mid + 1
        else :
            ans = mid
            right = mid - 1

    return ans
