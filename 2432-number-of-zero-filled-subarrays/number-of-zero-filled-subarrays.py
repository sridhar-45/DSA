class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        length = 0
        cnt = 0

        for num in nums:
            if num == 0:
                length += 1

            else:
                length = 0
        

            cnt += length
        
        return cnt
          