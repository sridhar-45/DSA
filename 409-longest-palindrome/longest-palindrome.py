from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        odd = False

        for val in freq.values():
            res += (val // 2) * 2
            if val % 2 == 1:
                odd = True

        return res + (1 if odd else 0)
