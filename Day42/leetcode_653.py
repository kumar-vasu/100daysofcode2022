# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):
        
        if not root:
            return {}
        
        nodes = { root.val : 1 }
        
        left = {}
        right = {}
        
        if root.left:
            left = self.traverse(root.left)
            
        if root.right:
            right = self.traverse(root.right)
            
        for key in right.keys():
            if key in nodes:
                nodes[key] += right[key]
            else:
                nodes[key] = right[key]
        
        for key in left.keys():
            if key in nodes:
                nodes[key] += left[key]
            else:
                nodes[key] = left[key]
        
        return nodes
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        nodes = self.traverse(root)
        print(nodes)
        for key in nodes.keys():
            if ( k != 2*key and k - key in  nodes ) or (k == 2*key and nodes[key] > 1):
                return True
        
        return False
        