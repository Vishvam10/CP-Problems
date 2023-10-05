"""
DIFFICULTY : easy
TAGS : array, string
"""
class Solution:
    def arrayStringsAreEqual(self, arr1: List[str], arr2: List[str]) -> bool:
        return "".join(arr1) == "".join(arr2)
        