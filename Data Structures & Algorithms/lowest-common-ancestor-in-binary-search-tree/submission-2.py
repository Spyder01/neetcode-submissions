# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return root
        
        if root.val in  (q.val, p.val):
            return root

        right, left = None, None
        if root.val < p.val or root.val < q.val:
            right = self.lowestCommonAncestor(root.right, p, q)
        
        if root.val > p.val or root.val > q.val:
            left = self.lowestCommonAncestor(root.left, p, q)

        if left and right:
            return root
        
        if left:
            return left
        
        return right

        