class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums) 
        if n <= 3:
            return sum(nums)

        nums[1:n] = sorted(nums[1:n])
        first = nums[0]
        second = nums[1]
        third = nums[2]

        return first + second + third    