# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        # ans = []
        # def dfs(root, val):
        #     if not root.left and not root.right:
        #         ans.append(int(val))
        #         return 
            
        #     if root.left:
        #         dfs(root.left, val + str(root.left.val))
            
        #     if root.right:
        #         dfs(root.right, val + str(root.right.val))
        

        # dfs(root, str(root.val))
        # return sum(ans)


        if not root:
            return 0

        def dfs(root, curr):
            if not root:
                return 0
            
            curr = curr * 10 + root.val

            if not root.left and not root.right:
                return curr
            
            return dfs(root.left, curr) + dfs(root.right, curr)

        return dfs(root, 0)