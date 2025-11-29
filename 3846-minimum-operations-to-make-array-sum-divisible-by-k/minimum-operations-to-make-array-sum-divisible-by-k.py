class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        if total == k:
            return 0
        elif total < k :
            return total
        
        res = 0
        while total % k != 0:
            res += 1
            total -= 1
        return res