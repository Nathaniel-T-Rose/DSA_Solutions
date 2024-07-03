# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levelQueue=[]
        result=[]
        levelQueue.append(root)
        while levelQueue!=[]:
            #get number in level
            for i in range(len(levelQueue)):
                node=levelQueue.pop(0) #add all new nodes to queue for next level
                if node and node.left!=None:
                    levelQueue.append(node.left)
                if node and node.right!=None:
                    levelQueue.append(node.right)
            # node now holds farthest right node of previous level
            if node:
                result.append(node.val) 
        return result

#solution: the wording on this is weird, need to return a list of furthest right node at each depth
#which won't necessarily be all of the furthest right