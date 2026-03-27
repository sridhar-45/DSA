class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i , num in enumerate(nums):
            val = target - num
            if val in seen:
                return [seen[val], i]
            else:
                seen[num] = i
        return [-1, -1]