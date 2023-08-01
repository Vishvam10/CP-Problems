class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        n = len(arr)
        arr.sort(key=lambda x: len(x))

        check = arr[0]
        m = len(check)
        c = m

        for word in arr :
            for i in range(len(check)) :
                if(word[i] != check[i]) :
                    c = min(c, i)
                    break
                
            # print('word, c : ', word, c)
        return check[:c]




