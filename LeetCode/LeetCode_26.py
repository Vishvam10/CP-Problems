class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:

        # Overwrite using 2 pointers
        n = len(arr)
        ptr = 0
        for i in range(1, n, 1) : 
            # print('arr, ptr, i : ', arr, ptr, i)
            if(arr[i] != arr[ptr]) :
                ptr += 1
                # print('overwrite : ', i, ptr)
                arr[ptr] = arr[i]
        return ptr + 1

        # Mark and swap
        # Doesn't work because the marker is not in the constraints

        # n = len(arr)
        # k = 0
        # ptr = 1
        # marker = False

        # for i in range(1, n, 1) :
        #     temp = arr[i-1]
        #     if(arr[i-1] == arr[i]) :
        #         ptr = i
        #         while(ptr < n) :
        #             if(temp == arr[ptr]) :
        #                 arr[ptr] = marker
        #                 ptr += 1
        #             else :
        #                 break
                
        # for i in range(1, n, 1) :
        #     if(arr[i] == marker) :
        #         for j in range(i, n, 1) :
        #             if(arr[j] != marker) :
        #                 break
 
        #         arr[i], arr[j] = arr[j], arr[i]

        # for i in range(n) :
        #     if(arr[i] != marker) :
        #         k += 1
        #     else :
        #         break
    
      
        # return k