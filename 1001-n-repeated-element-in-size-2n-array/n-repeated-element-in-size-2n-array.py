from collections import Counter 
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = Counter(nums)

        for key ,val in freq.items():
            if val * 2 == len(nums):
                return key
        
        return -1