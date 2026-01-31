class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        for i, val in enumerate(letters):
            if ord(val) > ord(target):
                return val
        
        return letters[0]