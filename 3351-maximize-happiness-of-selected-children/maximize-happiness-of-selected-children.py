class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        decrease = 0
        res = 0

        for i in range(k):
            curr = happiness[i] - decrease
            if curr <= 0:
                break
            res += curr
            decrease += 1
        
        return res
