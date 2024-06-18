class MinStack:
    #track current min val of each node
    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if self.stack==[]:
            mini=val
        else:
            mini=min(val,self.getMin())
        self.stack=[Node(val,mini)]+self.stack
        

    def pop(self) -> None:
        self.stack=self.stack[1:]

    def top(self) -> int:
        return self.stack[0].val    

    def getMin(self) -> int:
        return self.stack[0].mini
        

class Node:
    def __init__(self,val,mini):
        self.val=val
        self.mini=mini