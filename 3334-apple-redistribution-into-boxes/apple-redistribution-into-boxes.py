class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        total = sum(apple)

        res = 0
        for n in capacity:
            if total > 0:
                total -= n
                res += 1
            else:
                return  res
        
        return res