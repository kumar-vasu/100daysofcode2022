class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        mapped = {}
        ans = set()
        def duplicated(node):
            if not node:
                return '#'
            s = ''
            if not node.left and not node.right:
                s += str(node.val)
                mapped[s] = mapped.get(s,0)+1
                if mapped[s]==2:
                    ans.add(node)
                return s
            s  = s + str(node.val)
            s = s + "," + duplicated(node.left)
            s = s+ "," + duplicated(node.right)
            mapped[s]  = mapped.get(s,0)+1
            if mapped[s]==2:
                ans.add(node)
            return s
        
        duplicated(root)
        return ans