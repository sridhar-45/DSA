class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i , j):
            if grid[i][j] != '1':
                return
            if (i, j) in seen:
                return 
            seen.add((i,j))   
            dire = [(0,1), (0,-1), (1,0), (-1, 0)]
            for dx, dy in dire:
                x = dx + i
                y = dy + j

                if 0 <= x < n and 0 <= y < m and (x,y) not in seen:
                    dfs(x,y)
        

        n = len(grid)
        m = len(grid[0])
        res = 0
        seen = set()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in seen:
                    res += 1
                    dfs(i, j)
        
        return res
                    