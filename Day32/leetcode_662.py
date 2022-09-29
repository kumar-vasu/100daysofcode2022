# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        stack = [root]
        max_ = 1
        
        while len(stack) != 0:
            
            len_ = len(stack)
            
            for i in range(len_):
                curr = stack.pop(0)
                
                if curr:
                    stack.append(curr.left)
                    stack.append(curr.right)
                else:
                    stack.append(None)
                    stack.append(None)
            
            while len(stack) > 0 and not stack[-1]:
                stack.pop(-1)
            max_ = max(max_ , len(stack))
        return max_
                
                