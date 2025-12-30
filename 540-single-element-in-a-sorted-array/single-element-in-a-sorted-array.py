class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # base intension is pair is starts at even until one odd value find .....
            if mid% 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                left = mid +2
            else:
                right = mid
        
        return nums[left]