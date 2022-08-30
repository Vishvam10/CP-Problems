from functools import cmp_to_key
class Solution:

	def printLargest(self,arr):
	    arr = [str(x) for x in arr]
	    def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
	    arr = sorted(arr, key=cmp_to_key(compare))
	    return ''.join(arr)
