# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def Traverse(self, root):
                
        if not root:
            return [True, set()]
        
        left = [True, set()]
        if root.left:
            left = self.Traverse(root.left)
            
            if left[0] == False:
                return [False, set()]
        
        right = [True, set()]
        if root.right:
            right = self.Traverse(root.right)
            
            if right[0] == False:
                return [False, set()]
            
        for i in left[1]:
            if i >= root.val:
                return [False, set()]
            
        for i in right[1]:
            if i <= root.val:
                return [False, set()]
        
        u = set()
        u = u.union(left[1], right[1], set([root.val]))
        
        return [True, u]
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.Traverse(root)[0]
