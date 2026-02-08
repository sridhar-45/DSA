# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(root):
            if not root:
                return 0
            lh = maxDepth(root.left)
            rh = maxDepth(root.right)

            return 1 + max(lh , rh)
            
        
        if not root:
            return True
        
        lh = maxDepth(root.left)
        rh = maxDepth(root.right)

        if abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        return False
