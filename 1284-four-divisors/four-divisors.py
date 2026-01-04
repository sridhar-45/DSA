from math import sqrt
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def numOfDivisors(num):
            ans = 0
            total = 0
            for i in range(1,int(sqrt(num)) + 1):
                if num % i == 0:
                    d1 = i
                    d2 = num // i # i * (n//i) = n this the logic...

                    ans += 1
                    total += d1

                    if d1 != d2:
                        ans += 1
                    total += d2

                if ans > 4:
                    return 0
            
            return total if ans == 4 else 0
        
        
        sol = 0
        mpp = [-1] * len(nums)
        for num in nums:
            val = numOfDivisors(num)
            if val:
                sol += val
        
        return sol

            