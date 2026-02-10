# from typing import List

# class Solution:
#     def longestBalanced(self, nums: List[int]) -> int:
#         n = len(nums)
#         maxi = 0
        
#         for i in range(n):
#             even_set = set()
#             odd_set = set()
            
#             for j in range(i, n):
#                 if nums[j] % 2 == 0:
#                     even_set.add(nums[j])
#                 else:
#                     odd_set.add(nums[j])
                
#                 if len(even_set) == len(odd_set):
#                     maxi = max(maxi, j - i + 1)
        
#         return maxi



from typing import List
from collections import defaultdict

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = 0

        for i in range(n):
            even_freq = defaultdict(int)
            odd_freq = defaultdict(int)
            even_unique = 0
            odd_unique = 0

            for j in range(i, n):
                num = nums[j]
                if num % 2 == 0:
                    if even_freq[num] == 0:
                        even_unique += 1
                    even_freq[num] += 1
                else:
                    if odd_freq[num] == 0:
                        odd_unique += 1
                    odd_freq[num] += 1

                if even_unique == odd_unique:
                    maxi = max(maxi, j - i + 1)

        return maxi
