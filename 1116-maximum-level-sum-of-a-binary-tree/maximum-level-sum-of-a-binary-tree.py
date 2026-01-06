# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        if not root.left and not root.right:
            return 1
        
        ans = 1
        maxi = root.val
        nodes = [root]
        level = 1
        while nodes:
            levels = []
            total = 0

            for node in nodes:
                total += node.val
                if node.left:
                    levels.append(node.left)
                if node.right:
                    levels.append(node.right)
            
            if total > maxi:
                maxi = total
                ans = level

            nodes = levels
            level += 1 # increase the level also
        
        return ans