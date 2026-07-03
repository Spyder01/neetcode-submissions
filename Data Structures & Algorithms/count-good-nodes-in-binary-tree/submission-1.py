# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        nodes = 0

        def dfs(root, prev):
            nonlocal nodes
            
            if root is None:
                return
            
            # Check if the current node is a "good" node
            if root.val >= prev:
                nodes += 1
                prev = root.val
            
            # Traverse left and right subtrees
            dfs(root.left, prev)
            dfs(root.right, prev)

        # Start DFS from root with a very small initial value
        dfs(root, -101)
        
        return nodes


        