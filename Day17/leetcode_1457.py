class Solution:
    def traverse (self, root):
        if not root:
            return [{}]
        
        if not root.left and not root.right:
            return [{str(root.val):1}]
        
        value = str(root.val) 
        if root.left:
            l_paths = self.traverse(root.left)
            for i in range(len(l_paths)):
                if str(root.val) in l_paths[i]:
                    l_paths[i][value] += 1
                else:
                    l_paths[i][value] = 1
            
        if root.right:
            r_paths = self.traverse(root.right)
            for i in range(len(r_paths)):
                if str(root.val) in r_paths[i]:
                    r_paths[i][str(root.val)] += 1
                else:
                    r_paths[i][str(root.val)] = 1
        
        if not root.left:
            return r_paths
        if not root.right:
            return l_paths
        
        paths = l_paths + r_paths
        
        return paths
        
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        paths = self.traverse(root)
        
        count = 0
        for i in range(len(paths)):
            odd = 0
            for j in paths[i].keys():
                if paths[i][j] % 2 == 1:
                    odd += 1
            if odd <= 1:
                count += 1
                
        return count