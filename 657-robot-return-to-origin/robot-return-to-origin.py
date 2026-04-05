class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # directions = {
        #     'U' : (-1, 0),
        #     'D' : (1, 0),
        #     'L' : (0, -1),
        #     'R' : (0, 1)
        # }

        # x = y =  0
        # for char in moves:
        #     dx, dy = directions[char]

        #     x += dx
        #     y += dy
    
        # return x == 0 and y == 0         
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")   