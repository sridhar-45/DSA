class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        mpp = defaultdict(list)
        ans = inf
        for ind, num in enumerate(nums):
            if len(mpp[num]) >= 2:
                ans = min(ans, ind - mpp[num][-2])
            mpp[num].append(ind)
        
        return ans * 2 if ans != inf else -1