class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return 1+self.countNodes(root.left) + self.countNodes(root.right) if root else 0
