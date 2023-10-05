#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        arr.sort(key=lambda x: x.value/x.weight, reverse=True)
        ans = 0
        for x in arr :
            if(x.weight < W) :
                ans += (x.value)
                W -= x.weight
            else :
                ans += (x.value / x.weight) * W
                W = 0
                break
        return ans