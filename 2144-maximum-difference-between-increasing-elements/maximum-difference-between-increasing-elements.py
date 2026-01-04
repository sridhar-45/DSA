class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxis = [0] * len(nums)
        maxis[len(nums)-1] = nums[-1] 
        for i in range(len(nums)-2, -1, -1):
            maxis[i] = max(maxis[i+1], nums[i])
        print(maxis)
        
        maxi = 0
        for i, val in enumerate(nums):
            maxi = max(maxis[i] - val, maxi)
        return maxi if maxi else -1