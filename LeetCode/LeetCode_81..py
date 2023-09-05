class Solution:
    def search(self, arr: List[int], x: int) -> bool:
        # Can't be done in O(logn) because removing the duplicates 
        # will take O(n) time anyway. 
        return True if x in arr else False