from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()  # Step 1: Sort array
        
        n = len(arr)
        min_diff = float('inf')
        
        # Step 2: Find minimum difference between adjacent elements
        for i in range(1, n):
            min_diff = min(min_diff, arr[i] - arr[i-1])
        
        # Step 3: Collect pairs with minimum difference
        ans = []
        for i in range(1, n):
            if arr[i] - arr[i-1] == min_diff:
                ans.append([arr[i-1], arr[i]])
        
        return ans
