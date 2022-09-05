# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while len(stack) > 0:
            
            curr_len = len(stack)
            
            for i in range(curr_len):
                curr_node = stack.pop(0)
                
                curr = []
                
                if curr_node.right:
                    curr.append(curr_node.right)
                
                if curr_node.left:
                    curr.append(curr_node.left)
                    
                stack = curr + stack
                        
                result = [curr_node.val] + result
            
        return result