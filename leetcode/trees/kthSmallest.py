# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        node=root
        count=0
        #modified dfs
        #go as far left as possible, then pop off
        #skips nones while stack still has nodes
        while node!=None or stack!=[]:
            while node!=None:
                stack.append(node)
                node=node.left
            node=stack.pop()
            count+=1
            if count==k:
                return node.val
            #explore potential children before backtracking
            node=node.right



        