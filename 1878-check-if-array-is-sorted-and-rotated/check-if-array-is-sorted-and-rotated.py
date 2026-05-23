class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return False
        count_breaks = 0

        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                count_breaks += 1
            

        return count_breaks <= 1

        