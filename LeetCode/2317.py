class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        
        # NOTE THAT x is arbitary i.e not necessarily from the arr   

        # 1. A[i] & (A[i] ^ x) enable you to turn 1-bit to 0-bit 
        # from A[i] since x is arbitrary.

        # 2. For an array contains all 1, if the count is even, 
        # XOR operation gives you 0, otherwise 1.

        # 3. Therefore, the question is equivalent to: if you can 
        # convert any digit from 1 to 0 for any number, 
        # what is the max for XOR(A[i]) for all i in len(nums)

        # 4. The max we can get is of course to make every digit of 
        # the answer to be 1 if possible (not if a digit is 0 for 
        # all number, there is nothing we can do).

        # 5. Therefore, OR(A[i]) is an approach.

        # ans = 0
        # for i in range(len(nums)) :
        #     ans = ans | nums[i]
        # return ans

        return reduce(ior, nums)

