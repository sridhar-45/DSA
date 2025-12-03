
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = int(10 ** 9 + 7)

        freq_dict = dict()

        for x, y in points:
            if y not in freq_dict:
                freq_dict[y] = 1
            else:
                freq_dict[y] += 1
        
        res = 0
        prevHorizontalLines = 0

        for key, val in freq_dict.items():
            cnt = val
            horizontalLines = cnt * (cnt - 1) // 2 #equal to ncr 
            res += horizontalLines * prevHorizontalLines
            prevHorizontalLines += horizontalLines

        return res % mod