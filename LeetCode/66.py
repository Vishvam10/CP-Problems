class Solution:
    # BASIC IDEA :
    
    # If last element is 9, make it 0, make the 
    # last element the second last element and
    # check again
    # If last element is not 9, add 1
    # If we have come to the 1st element and it 
    # is 9, make it 0 and add [1] to the final list
    
#     RECURSIVE IMPLEMENTATION :

#     def plusOne(self, arr: List[int]) -> List[int]:
#         if len(arr) == 0:
#             arr = [1]
#         elif arr[-1] == 9:
#             arr = self.plusOne(arr[:-1])
#             arr.extend([0])
#         else:
#             arr[-1] += 1
#         return arr

#      ITERATIVE IMPLEMENTATION
    
     def plusOne(self, arr: List[int]) -> List[int]:
        arr[-1] += 1
        for i in range(len(arr)-1, 0, -1) :
            if(arr[i] != 10) :
                break
            arr[i] = 0
            arr[i-1] += 1
        if(arr[0] == 10) :
            arr[0] = 0
            arr = [1] + arr
        return arr


            