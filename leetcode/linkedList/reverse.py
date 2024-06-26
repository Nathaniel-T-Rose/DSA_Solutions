def reverseList(self, head):
        prev=None
        hold=None
        while head !=None:
            hold=head.next
            head.next=prev
            prev=head
            head=hold
        return prev