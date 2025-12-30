class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        start = -1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                right = mid -1
                start = mid
            
            elif nums[mid] < target:
                left = mid + 1
            else: 
                right = mid - 1
        

        end = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                left = mid + 1
                end = mid
            
            elif nums[mid] < target:
                left = mid+1
            else: 
                right = mid - 1
    
        return [start , end]