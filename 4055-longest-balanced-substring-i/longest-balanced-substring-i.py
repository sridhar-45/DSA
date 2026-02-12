class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        maxi = 0
        
        for i in range(n):
            freq = [0] * 26
            distinct = 0
            max_freq = 0
            
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                
                if freq[idx] == 0:
                    distinct += 1
                
                freq[idx] += 1
                max_freq = max(max_freq, freq[idx])
                
                length = j - i + 1
                
                # Check balanced condition
                if length == max_freq * distinct:
                    maxi = max(maxi, length)
        
        return maxi
