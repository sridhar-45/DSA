# class Solution:
#     def minOperations(self, s: str) -> int:
#         start_with_0 = 0 # 01010101..
#         start_with_1 = 0 # 10101010...

#         n = len(s)
#         for i in range(n):
#             if i % 2== 0:
#                 if s[i] == "0":
#                     start_with_1 += 1
#                 else:
#                     start_with_0 += 1
#             else:
#                 if s[i] == "1":
#                     start_with_1 += 1
#                 else:
#                     start_with_0 += 1
            
#         return min(start_with_1, start_with_0)



###### simpel another approach ...
class Solution:
    def minOperations(self, s: str) -> int:
        start_with_0 = 0 # 01010101..
        
        n = len(s)
        for i in range(n):
            if i % 2== 0:
                if s[i] == "1":
                    start_with_0 += 1
            else:
                if s[i] == "0":
                    start_with_0 += 1
            
        return min(start_with_0, n - start_with_0)