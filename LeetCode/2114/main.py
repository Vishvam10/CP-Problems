class Solution:
    def mostWordsFound(self, arr: List[str]) -> int:
        return max([len(x.split()) for x in arr])
