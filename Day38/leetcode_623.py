# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        
        queue = [root]
        
        while len(queue) > 0 and depth > 1:
            depth -= 1
            curr_len = len(queue)
            for i in range(curr_len):
                curr = queue.pop(0)
                if depth == 1:
                    new_node_left = TreeNode(val)
                    new_node_left.left = curr.left
                    new_node_right = TreeNode(val)
                    new_node_right.right = curr.right
                    curr.left = new_node_left
                    curr.right = new_node_right
                else:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
        return root 
                