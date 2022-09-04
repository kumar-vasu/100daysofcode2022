# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Traversal(self, root, curr, traversal):
        
        row = curr[0]
        col = curr[1]
        
        if root.left:
            if (row - 1, col +1) in traversal:
                traversal[(row - 1, col +1)].append(root.left.val)
                traversal[(row - 1, col +1)] = sorted(traversal[(row - 1, col +1)])
            else:
                traversal[(row - 1, col +1)] = [root.left.val]
            traversal = self.Traversal(root.left, [row - 1, col +1], traversal)
            
        if root.right:
            if (row + 1, col +1) in traversal:
                traversal[(row + 1, col +1)].append(root.right.val)
                traversal[(row + 1, col +1)] = sorted(traversal[(row + 1, col +1)])
            else:
                traversal[(row + 1, col +1)] = [root.right.val]
            traversal = self.Traversal(root.right, [row + 1, col +1], traversal)
        
        return traversal
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        traversal = {(0,0) : [root.val]}
        traversal = self.Traversal(root, [0,0], traversal)
        
        keys_list = sorted(list(traversal.keys()))
        
        result = []
        
        for i in range(len(keys_list)):
            #print(keys_list[i], traversal[keys_list[i]])
            if len(result) == 0:
                result.append(traversal[keys_list[i]])
                
            elif keys_list[i-1][0] == keys_list[i][0]:
                result[-1].extend(traversal[keys_list[i]])
            
            else:
                result.append(traversal[keys_list[i]])
            
        return result