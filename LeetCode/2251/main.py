class Solution:
    # Keep all start and end in 2 arrays and sort them.
    # IDEA : Kinda like merging intervals OR
    #   The bsearch on STARTED is basically the total number of flowers the person would have
    #   seen if they didn't die at all and
    #   The bsearch on ENDED is the flowers that actually die and is hence subtracted from
    #   the answer

    # For each time point t in persons:
    #   Binary search the upper bound of t in start, then we find the started flowers.
    #   Binary search the lower bound of t in end, then we find the started flowers.

    #   Blooming flowers = started flowers - ended flowers

    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        #         ans = [0]*len(persons)
        #         for i in range(len(persons)) :
        #             p = persons[i]

        #             for start, end in flowers :
        #                 if(p >= start and p <= end) :
        #                     ans[i] += 1
        #         return ans
        start = sorted(a for a, b in flowers)
        end = sorted(b for a, b in flowers)
        return [bisect_right(start, t) - bisect_left(end, t) for t in persons]
