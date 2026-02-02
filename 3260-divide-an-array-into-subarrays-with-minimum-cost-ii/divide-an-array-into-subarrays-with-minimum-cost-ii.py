from bisect import bisect_left, insort

class Solution:
    def minimumCost(self, nums, k, dist):
        n = len(nums)

        # These lists will stay sorted as (value, index)
        kMinimum = []      # stores k-1 smallest elements
        remaining = []     # stores the rest

        total_sum = 0
        i = 1

        # Build first window [1 ... dist+1]
        while i < n and i - dist < 1:
            cur = (nums[i], i)
            insort(kMinimum, cur)
            total_sum += nums[i]

            if len(kMinimum) > k - 1:
                largest = kMinimum.pop()
                total_sum -= largest[0]
                insort(remaining, largest)

            i += 1

        result = float("inf")

        # Sliding window
        while i < n:
            cur = (nums[i], i)
            insort(kMinimum, cur)
            total_sum += nums[i]

            if len(kMinimum) > k - 1:
                largest = kMinimum.pop()
                total_sum -= largest[0]
                insort(remaining, largest)

            result = min(result, total_sum)

            # Remove expired index (i - dist)
            rem_idx = i - dist
            to_remove = (nums[rem_idx], rem_idx)

            pos = bisect_left(kMinimum, to_remove)
            if pos < len(kMinimum) and kMinimum[pos] == to_remove:
                kMinimum.pop(pos)
                total_sum -= nums[rem_idx]

                if remaining:
                    promote = remaining.pop(0)
                    insort(kMinimum, promote)
                    total_sum += promote[0]
            else:
                pos = bisect_left(remaining, to_remove)
                if pos < len(remaining) and remaining[pos] == to_remove:
                    remaining.pop(pos)

            i += 1

        return nums[0] + result
