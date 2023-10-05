def floorSqrt(n):
   # write your code logic here .

   low, high = 0, n
   while(low <= high) :
      mid = low + (high - low) // 2
      if(mid * mid == n) :
         return mid
      if(mid * mid > n) :
         high = mid - 1
      else :
         low = mid + 1
   return high

n= int(input())
print(floorSqrt(n))