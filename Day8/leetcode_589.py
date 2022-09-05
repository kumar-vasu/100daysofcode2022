"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while len(stack) > 0:
            
            curr_len = len(stack)
            
            for i in range(curr_len):
                curr_node = stack.pop(0)
                
                if curr_node.children:
                    curr = []
                    for node in curr_node.children:
                        curr.append(node)
                    stack = curr + stack
                        
                result.append(curr_node.val)
            
        return result