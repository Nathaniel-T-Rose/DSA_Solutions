# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue=[] #(node,maxVal)
        queue.append((root,root.val))
        total=0

        while queue!=[]:
            node,maxVal=queue.pop(0)
            if node:
                if node.val>=maxVal:
                    total+=1
                    maxVal=node.val
                if node.left:
                    queue.append((node.left,maxVal))
                if node.right:
                    queue.append((node.right,maxVal))
        return total



        