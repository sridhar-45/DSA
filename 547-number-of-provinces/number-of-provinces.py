class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = set()

        def dfs(node):
            if node not in visited:
                visited.add(node)
                
                for neighbor in range(len(isConnected)):
                    if isConnected[node][neighbor] == 1 and neighbor not in visited:
                        dfs(neighbor)
            

        for node in range(len(isConnected)):
            if node not in visited:
                res += 1
                dfs(node)
    
        return res
