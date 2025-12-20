class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0

        n = len(strs)
        m = len(strs[0])

        for c in range(m):
            curr_char = strs[0][c]
            for r in range(1, n):
                if curr_char > strs[r][c]:
                    res += 1
                    break
                curr_char = strs[r][c]
        return res