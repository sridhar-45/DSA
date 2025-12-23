class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        rows = len(strs)
        cols = len(strs[0])

        alreadySorted = [False] * (rows - 1)

        for c in range(cols):
            flag = True

            for r in range(rows - 1):
                if not alreadySorted[r] and strs[r][c] > strs[r + 1][c]:
                    res += 1
                    flag = False
                    break

            if not flag:
                continue

            for r in range(rows - 1):
                if strs[r][c] < strs[r + 1][c]:
                    alreadySorted[r] = True

        return res
