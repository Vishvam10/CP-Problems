class Solution:
    def countGoodNumbers(self, n: int) -> int:

        mod = 1000000007
        '''
        Even indices => Even digit (0, 2, 4, 5, 8)
        Odd indices => Prime (2, 3, 5, 7)
        _,_,_,_,_,_
        5,4,5,4,5,4

        ((a*b)%c) = ((a%c)*(b%c)%c)
        '''
        ev, od = (n + 1) // 2, n // 2

        # Ideally, binary exponentiation would be preferred
        ans = (pow(5, ev, mod) * pow(4, od, mod)) % mod

        return ans
