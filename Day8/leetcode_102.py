# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = [root]
        result = []
        
        while len(queue) > 0:
            
            curr_len = len(queue)
            curr = []
            for i in range(curr_len):
                curr_node = queue.pop(0)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                    
                if curr_node.right:
                    queue.append(curr_node.right)
                        
                curr.append(curr_node.val)
                
            result.append(curr)
            
        return result