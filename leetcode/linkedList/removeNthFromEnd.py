def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        prev=None
        #find length
        length=0
        while cur!=None:
            cur=cur.next
            length+=1
        cur=head
        for i in range(length-n):
            prev=cur
            cur=cur.next
        if prev==None:
            #no previous node for nth from end
            #remove first element
            head=cur.next
        elif cur==None:
            #remove last element
            prev.next=None
        else:
            #remove intermediate element
            prev.next=cur.next
        return head