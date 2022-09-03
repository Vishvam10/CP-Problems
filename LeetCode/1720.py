class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # XOR is self-inverting (also, commutative and associative)
        # So, if a XOR b = c, then c XOR a = b and c XOR b = a.
        # Also, a XOR b = c is the same as b XOR a = c
        
        ans = []
        ans.append(first ^ encoded[0])
        for i in range(1, len(encoded)) :
            ans.append(encoded[i] ^ ans[i-1])
        ans.insert(0, first)
        return ans
    
        # ans = [first]
        # for i in range(len(encoded)):
        #     ans.append(ans[-1] ^ encoded[i])
        # return ans