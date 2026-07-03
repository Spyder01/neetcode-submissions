# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return (True, 0)

            r_bal, r_height = dfs(root.right)
            l_bal, l_height = dfs(root.left)


            bal = r_bal and l_bal and abs(r_height - l_height) <= 1
            return bal, 1 + max(l_height, r_height) 
        
        return dfs(root)[0]
        