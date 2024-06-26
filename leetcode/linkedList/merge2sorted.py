def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0,None)
        current=head
        while list1!=None and list2!=None:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        if list1!=None:
            current.next=list1
        if list2!=None:
            current.next=list2

        return head.next
        
