class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # left = 0 
        # right = len(nums) - 1

        # while left < right:
        #     mid = (left + right) // 2

        #     # base intension is pair is starts at even until one odd value find .....
        #     if mid% 2 == 1:
        #         mid -= 1
            
        #     if nums[mid] == nums[mid + 1]:
        #         left = mid +2
        #     else:
        #         right = mid
        
        # return nums[left]



    
        n = len(nums)
    
        if len(nums) == 1: return nums[0]
        if nums[0] != nums[1] : return nums[0]
        if nums[n-1] != nums[n-2] : return nums[n-1]
         
        left = 0
        right = n-2 
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            
            if (mid%2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2  and nums[mid] == nums[mid-1]):
                left = mid + 1
            else:
                right = mid - 1

        return -1 

