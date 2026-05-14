from collections import Counter
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
            
        freq = Counter(nums)
        for i in range(1, n):
            if i not in freq:
                return False
            elif i != (n-1) and freq[i] > 1:
                return False
            elif i == (n-1) and freq[i] != 2:
                return False
            
        return True