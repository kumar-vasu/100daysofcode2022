# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root 
        
        if root.left:
            p_left = self.pruneTree(root.left)
            root.left = p_left
            
        if root.right:
            p_right = self.pruneTree(root.right) 
            root.right = p_right
        
        if root.left == None and root.right == None and root.val == 0:
            return None
        
        return root