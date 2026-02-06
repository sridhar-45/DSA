from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        maxEl = nums[0]
        minEl = nums[0]

        L = 1
        i = 0
        j = 0

        while j < n:
            maxEl = nums[j]
            minEl = nums[i]

            while i < j and maxEl > k * minEl:
                i += 1
                minEl = nums[i]

            L = max(L, j - i + 1)
            j += 1

        return n - L
