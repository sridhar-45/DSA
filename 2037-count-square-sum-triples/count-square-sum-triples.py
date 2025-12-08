from math import isqrt

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0

        for a in range(1, n+1):
            for b in range(1, n+1):
                c2 = a*a + b*b
                c = isqrt(c2)

                if c <= n and c * c == c2:
                    res += 1

        return res
