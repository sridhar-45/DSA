# class Solution:
#     def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
#         res = []

#         for query in  queries:
#             start, end = query
#             cnt = 0
#             plates_cnt= 0
#             s_candle = -1
#             for i in range(start, end+1):
#                 if s[i] == "|" and s_candle == -1:
#                     s_candle = 1
#                 if s_candle == 1 and s[i] =="|":
#                     plates_cnt += cnt
#                     cnt = 0
#                 if s_candle == 1 and s[i] == "*":
#                     cnt += 1
#             res.append(plates_cnt)
#         return res


from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # 1. Pre-process: Candle Indices and Plate Prefix Sums (O(N))
        candle_indices = [] 
        plate_prefix_sum = [0] * (n + 1)
        
        plate_count = 0
        for i in range(n):
            if s[i] == '|':
                candle_indices.append(i)
            else:
                plate_count += 1
            
            plate_prefix_sum[i+1] = plate_count

        results = []
        
        # Manual Binary Search functions
        
        def find_first_candle_ge(target_index: int) -> int:
            """Finds the index in candle_indices of the first candle >= target_index."""
            c_len = len(candle_indices)
            low, high = 0, c_len - 1
            result_idx = c_len # Default: means no candle found
            
            while low <= high:
                mid = low + (high - low) // 2
                if candle_indices[mid] >= target_index:
                    result_idx = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return result_idx

        def find_last_candle_le(target_index: int) -> int:
            """Finds the index in candle_indices of the last candle <= target_index."""
            c_len = len(candle_indices)
            low, high = 0, c_len - 1
            result_idx = -1 # Default: means no candle found
            
            while low <= high:
                mid = low + (high - low) // 2
                if candle_indices[mid] <= target_index:
                    result_idx = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return result_idx

        # 2. Process Queries (O(Q log N))
        for start, end in queries:
            
            # Find the index in candle_indices array for the left bounding candle
            left_idx_in_arr = find_first_candle_ge(start)
            
            # Find the index in candle_indices array for the right bounding candle
            right_idx_in_arr = find_last_candle_le(end)

            
            # 3. Check Feasibility and Calculate
            
            # Must have at least two distinct candles
            if left_idx_in_arr >= right_idx_in_arr:
                results.append(0)
                continue
            
            # Get the actual index in string s of the bounding candles
            i_left = candle_indices[left_idx_in_arr] 
            i_right = candle_indices[right_idx_in_arr]
            
            # Count plates using prefix sums: 
            # plates_between = (Total plates up to i_right - Total plates up to i_left)
            plates_total = plate_prefix_sum[i_right] - plate_prefix_sum[i_left + 1]
            
            results.append(plates_total)
            
        return results