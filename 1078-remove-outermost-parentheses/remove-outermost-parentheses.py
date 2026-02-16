class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        res = []
        for char in s:
            if char == "(":
                if balance :
                    res.append("(")
                balance += 1
            else:
                balance -= 1
                if balance:
                    res.append(")")
        
        return "".join(res)
