class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k=len(nums)
        for i in range(0,k):
            j=i+1
            for j in range(j,k):

                if nums[i]+nums[j]==target:
                    return [i,j]                   