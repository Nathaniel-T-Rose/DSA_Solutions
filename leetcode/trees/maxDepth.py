def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        left=self.maxDepth(root.left)+1
        right=self.maxDepth(root.right)+1
        return max(left,right)