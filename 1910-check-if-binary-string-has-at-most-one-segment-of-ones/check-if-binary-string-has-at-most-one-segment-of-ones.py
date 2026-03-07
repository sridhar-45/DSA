class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)

        for i in range(n-2, -1, -1):
            if s[i] < s[i+1] :
                return False
        
        return True
