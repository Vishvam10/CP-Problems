class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        a = [arr1[i] + arr2[i] + i for i in range(len(arr1))]
        b = [arr1[i] + arr2[i] - i for i in range(len(arr1))]
        c = [arr1[i] - arr2[i] + i for i in range(len(arr1))]
        d = [arr1[i] - arr2[i] - i for i in range(len(arr1))]

        return max(map(lambda x: max(x) - min(x), (a, b, c, d)))


"""

abs(A) + abs(B) = max(A+B, A-B, -A+B, -A-B).

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

= max(
    (arr1[i] + arr2[i] + i) - (arr2[j] + arr2[j] + j),
    (arr1[i] + arr2[i] - i) - (arr1[j] + arr2[j] - j),
    (arr1[i] - arr2[i] + i) - (arr2[j] - arr2[j] + j),
    (arr1[i] - arr2[i] - i) - (arr1[j] - arr2[j] - j),
    
    // The other 4 cases are just symmetric
    
)

"""
