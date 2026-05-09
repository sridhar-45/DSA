# from typing import List
# class Solution:
#     def rotateTraverse(self,r, c, rows, cols , new_mat , mat):
#         curr_last_row = rows - r - 1
#         curr_last_col = cols - c - 1
#         # print("the current grid")
#         # self.print_mat(mat)
#         # print()
         
#         # print("the current new_mat")
#         # self.print_mat(new_mat)
#         # print()
        
#         #down traverse
#         # print("entering down traverse .....")
#         for i in range(r+1, rows - r):
#             new_mat[i][c] = mat[i-1][c]
        
#         #right traverse
#         # print("entering right traverse .....")
#         for i in range(r+1, cols - c):
#             new_mat[curr_last_row][i] = mat[curr_last_row][i-1]
            
#         #up traverse
#         # print("entering up traverse .....")
#         for i in range(curr_last_row - 1, r-1, -1):
#             new_mat[i][curr_last_col] = mat[i+1][curr_last_col]
        
#         #left traverse
#         # print("entering left traverse .....")
#         for i in range(curr_last_col - 1, c-1, -1):
#             new_mat[r][i] = mat[r][i+1]
        
        
#     def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:  
#         rows = len(grid)
#         cols = len(grid[0])

#         # n = cols // 2
#         n = min(rows, cols) // 2
#         new_mat = [[0] * cols for _ in range(rows)]
        
#         while k :
#             # print(f"\nrotateTraverse function calling......{k}")
#             new_mat = [row[:] for row in grid]
#             for i in range(n):
#                 self.rotateTraverse(i, i , rows , cols, new_mat ,grid)
#                 # self.print_mat(new_mat)
#                 # print()
            
#             k -= 1
#             grid = [row[:] for row in new_mat]
#             # print("the updated grid")
#             # self.print_mat(grid)
#             # print()
        
            
#         # self.print_mat(new_mat)
#         # print()
#         return new_mat
        
    
#     def print_mat(self, mat):
#         r = len(mat)
#         c = len(mat[0])
        
#         for i in range(r):
#             for j in range(c):
#                 print(mat[i][j], end = " ")
#             print()
    
    
    
# # obj = Solution()
# # grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# # k = 2
# # ans = obj.rotateGrid(grid, k)
# # # print("the result grid :")
# # obj.print_mat(ans)
            


from typing import List

class Solution:

    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        rows = len(grid)
        cols = len(grid[0])

        layers = min(rows, cols) // 2

        for layer in range(layers):

            elements = []

            top = layer
            left = layer
            bottom = rows - layer - 1
            right = cols - layer - 1

            # left column
            for i in range(top, bottom + 1):
                elements.append(grid[i][left])

            # bottom row
            for j in range(left + 1, right + 1):
                elements.append(grid[bottom][j])

            # right column
            for i in range(bottom - 1, top - 1, -1):
                elements.append(grid[i][right])

            # top row
            for j in range(right - 1, left, -1):
                elements.append(grid[top][j])

            rotate = k % len(elements)

            # FIXED ROTATION
            rotated = elements[-rotate:] + elements[:-rotate]

            idx = 0

            # left column
            for i in range(top, bottom + 1):
                grid[i][left] = rotated[idx]
                idx += 1

            # bottom row
            for j in range(left + 1, right + 1):
                grid[bottom][j] = rotated[idx]
                idx += 1

            # right column
            for i in range(bottom - 1, top - 1, -1):
                grid[i][right] = rotated[idx]
                idx += 1

            # top row
            for j in range(right - 1, left, -1):
                grid[top][j] = rotated[idx]
                idx += 1

        return grid





