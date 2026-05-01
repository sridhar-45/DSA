# class Solution:
#     def max_product(self, nums):
#         ans = 0
#         for i, num in enumerate(nums):
#             ans += i * num
#         return ans


#     def rotate(self,i, nums):
#         n = len(nums)
#         return nums[-i:] + nums[ : n-i]

#     def maxRotateFunction(self, nums: List[int]) -> int:

#         n = len(nums)
#         res = -inf
#         for i in range(n):
#             if i != 0:
#                 arr = self.rotate(i, nums)
#             else:
#                 arr = nums
#             val = self.max_product(arr)
#             res = max(val, res)
        
#         return res




from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        # F(0)
        f = sum(i * num for i, num in enumerate(nums))
        res = f
        
        for k in range(1, n):
            f = f + total_sum - n * nums[n - k]
            res = max(res, f)
        
        return res