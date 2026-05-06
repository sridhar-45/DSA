class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])
        
        for r in range(rows):
            ind = cols - 1

            for c in reversed(range(cols)):
                if box[r][c] == "#":
                    box[r][c],box[r][ind] = box[r][ind],box[r][c]
                    ind -= 1 # move the i th pointer to left side..

                elif box[r][c] == "*":
                    ind = c - 1 # move the ith pointer to left..of column

        res = []

        for c in range(cols):
            col = []
            for r in reversed(range(rows)):
                col.append(box[r][c])

            res.append(col)    


        return res        