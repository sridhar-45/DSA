# class Solution:
#     def maxSubarraySum(self, nums: List[int], k: int) -> int:
#         maxi = float("-inf")
#         n = len(nums)
#         for i in range(n):
#             total = 0
#             ind = 0
#             for j in range(i, n):
#                 total += nums[j]
#                 # print(total)
#                 ind += 1 
#                 if ind % k == 0:
#                     maxi = max(maxi, total)
        
#         return maxi
                

class Solution:
    def maxSubarraySum(self, nums, k):
        n = len(nums)

        # prefix sum array
        prefSum = [0] * n
        prefSum[0] = nums[0]
        for i in range(1, n):
            prefSum[i] = prefSum[i - 1] + nums[i]

        result = float("-inf")

        # iterate over all starting offsets from 0 ... k-1
        for start in range(k):
            currSum = 0
            i = start

            # i + k - 1 must be inside array (valid block)
            while i < n and i + k - 1 < n:
                j = i + k - 1

                # compute subarray sum nums[i ... j]
                subSum = prefSum[j] - (prefSum[i - 1] if i > 0 else 0)

                # Kadane’s idea on blocks of size k
                currSum = max(subSum, currSum + subSum)

                result = max(result, currSum)

                i += k  # jump by k to next block
        
        return result
