# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Traverse(self, root):
        if not root:
            return []
        
        left = []
        if root.left:
            left = self.Traverse(root.left)
            
        right = []
        if root.right:
            right = self.Traverse(root.right)
            
        u = left + right + [root.val]
        
        return u
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        ele = self.Traverse(root)
        
        count = {}
        
        for i in ele:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        max_ = -1
        result = []
        for i in count:
            if count[i] > max_:
                max_ = count[i]
                result = [i]
                
            elif count[i] == max_:
                result.append(i)
                
        return result