class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        # Overwrite using 2 pointers
        n = len(arr)
        ptr = 0
        for i in range(1, n, 1):
            # print('arr, ptr, i : ', arr, ptr, i)
            if arr[i] != arr[ptr]:
                ptr += 1
                # print('overwrite : ', i, ptr)
                arr[ptr] = arr[i]
        return ptr + 1
