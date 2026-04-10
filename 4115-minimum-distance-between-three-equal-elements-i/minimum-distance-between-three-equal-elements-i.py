from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3 :
            return -1
        
        # ans = inf
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] == nums[j] == nums[k]:
        #                 ans = min(ans , abs(i - j) + abs(j - k) + abs(k - i))

        # return ans if ans != inf else -1

        mpp = defaultdict(list)
        ans = inf
        for ind, num in enumerate(nums):
            if len(mpp[num]) >= 2:
                ans = min(ans, ind - mpp[num][-2])
            mpp[num].append(ind)
        
        return ans * 2 if ans != inf else -1
            