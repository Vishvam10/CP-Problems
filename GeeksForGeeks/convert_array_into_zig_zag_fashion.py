class Solution:

    def zigZag(self, arr, n):
        for i in range(n-1):
            if(i % 2 == 0):
                if(arr[i] > arr[i+1]):
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
            else:
                if(arr[i] < arr[i+1]):
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
        return arr
