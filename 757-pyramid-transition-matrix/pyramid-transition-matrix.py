from collections import defaultdict
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        def solve(curr: str, ind: int, above: str) -> bool:
            # Base case: reached the top
            if len(curr) == 1:
                return True

            # Finished building one level, move up
            if ind == len(curr) - 1:
                return solve(above, 0, "")

            pair = curr[ind] + curr[ind + 1]
            if pair not in mpp:
                return False

            for ch in mpp[pair]:
                if solve(curr, ind + 1, above + ch):
                    return True

            return False

        mpp = defaultdict(list)
        for x, y, z in allowed:
            mpp[x + y].append(z)

        return solve(bottom, 0, "")
