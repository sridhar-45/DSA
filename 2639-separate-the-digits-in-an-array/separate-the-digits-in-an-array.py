class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            for val in str(num):
                res.append(int(val))
        
        return res