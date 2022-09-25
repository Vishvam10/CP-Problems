class Solution:
    # First, do the merge procedure as it is. Only
    # difference here is that, instead of appending
    # to a new list, we start appending it to the end
    # of the first list.
    
    # Maintain one extra pointer (say, i) to denote the
    # next place to insert
    
    # THERE WILL BE OVERWRITES but none of the data is 
    # lost because by the time the pointer i gets to n or 
    # m, it would have already added the data before it 
    # to the end of nums1
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a,b,i = m-1, n-1, m+n-1
        
        while(b >= 0) :
            if(a >=0 and nums1[a] > nums2[b]) :
                nums1[i] = nums1[a]
                a -= 1
            else :
                nums1[i] = nums2[b]
                b -= 1
            i -= 1