"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        queue = [root]
        result = []
        
        while len(queue) > 0:
            
            curr_len = len(queue)
            curr = []
            for i in range(curr_len):
                curr_node = queue.pop(0)
                
                if curr_node.children:
                    
                    for node in curr_node.children:
                        queue.append(node)
                        
                curr.append(curr_node.val)
                
            result.append(curr)
            
        return result