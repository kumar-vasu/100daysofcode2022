class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def preorder(root,greatest):
            if not root:
                return
            greatest=max(greatest,root.val)
            if greatest<=root.val:
                nonlocal good
                good+=1
            preorder(root.left,greatest)
            preorder(root.right,greatest)
        
        good=0
        preorder(root,float("-inf"))
        return good
        