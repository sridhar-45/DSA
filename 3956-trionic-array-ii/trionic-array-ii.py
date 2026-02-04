from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        NEG = -10**18

        # dp[i][trend]
        dp = [[NEG] * 4 for _ in range(n + 1)]

        # Base case
        dp[n][3] = 0  # valid end
        # other dp[n][*] remain NEG

        for i in range(n - 1, -1, -1):
            curr = nums[i]

            # trend 0: skip or start increasing
            dp[i][0] = dp[i + 1][0]  # skip
            if i + 1 < n and nums[i + 1] > curr:
                dp[i][0] = max(dp[i][0], curr + dp[i + 1][1])

            # trend 1: increasing
            if i + 1 < n:
                if nums[i + 1] > curr:
                    dp[i][1] = curr + dp[i + 1][1]
                elif nums[i + 1] < curr:
                    dp[i][1] = curr + dp[i + 1][2]

            # trend 2: decreasing
            if i + 1 < n:
                if nums[i + 1] < curr:
                    dp[i][2] = curr + dp[i + 1][2]
                elif nums[i + 1] > curr:
                    dp[i][2] = curr + dp[i + 1][3]

            # trend 3: final increasing
            dp[i][3] = curr  # can always end here
            if i + 1 < n and nums[i + 1] > curr:
                dp[i][3] = max(dp[i][3], curr + dp[i + 1][3])

        return dp[0][0]
