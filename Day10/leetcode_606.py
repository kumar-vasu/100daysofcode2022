# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        if root == None:
            return None
        
        left_result = ""
        right_result = ""
        
        if root.left:
            left_result = "(" + self.tree2str(root.left) + ")"
            
        if root.right:
            right_result = "(" + self.tree2str(root.right) + ")"
            
        if right_result != "" and left_result == "":
            left_result = "()"
            
        return f"{root.val}"+left_result+right_result
            
        