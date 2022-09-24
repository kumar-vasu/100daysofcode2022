# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if not root:
            return []
        
        res = []
        
        if root.left:
            res.extend(self.binaryTreePaths(root.left))
            
        if root.right:
            res.extend(self.binaryTreePaths(root.right))
        
        if len(res) == 0:
            return [str(root.val)]
        
        else:
            return [str(root.val)+"->"+i for i in res]