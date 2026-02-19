class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0

        curr = 1
        prev = 0
         
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i-1]:
                curr += 1
            else:
                res += min(prev, curr)
                prev = curr
                curr = 1


        return res + min(prev, curr)        
                