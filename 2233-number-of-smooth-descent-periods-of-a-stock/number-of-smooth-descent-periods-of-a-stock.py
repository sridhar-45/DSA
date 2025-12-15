class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)

        def dfs(i, length):
            if i == n:
                return 0
            
            if i > 0 and prices[i-1] - prices[i] == 1:
                length += 1
            else:
                length = 1
            
            return length + dfs(i+1, length)
        
        return dfs(0, 0)