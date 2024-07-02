def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return root
        root.left=self.invertTree(root.left)
        root.right=self.invertTree(root.right)
        
        hold=root.left
        root.left=root.right
        root.right=hold
        return root
