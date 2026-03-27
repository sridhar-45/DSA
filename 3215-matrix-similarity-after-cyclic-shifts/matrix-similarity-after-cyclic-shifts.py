class Solution:
    def left_right_shifts(self, arr, n):
        res = []
        m = len(arr[0])
        for i in range(n):
            if i % 2 == 0:
                ans = arr[i][1:] + [arr[i][0]]
            else:
                ans = [arr[i][-1]] + arr[i][: m-1]
            res.append(ans)

        return res


    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat)
        copy_mat = [row[:] for row in mat]

        i = 0
        while i < k:
            copy_mat = self.left_right_shifts(copy_mat, n)
            i += 1
        
        return copy_mat == mat