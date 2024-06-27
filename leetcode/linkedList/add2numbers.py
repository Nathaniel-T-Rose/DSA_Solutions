def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        head=ListNode()
        current=head
        cur1=l1
        cur2=l2
        while cur1!=None or cur2!=None:
            if cur1==None:
                val1=0
                val2=cur2.val
                cur2=cur2.next
            elif cur2==None:
                val1=cur1.val
                val2=0
                cur1=cur1.next
            else:
                val1=cur1.val
                val2=cur2.val
                cur1=cur1.next
                cur2=cur2.next

            newVal=val1+val2+carry
            carry=newVal//10
            newVal=newVal%10
            current.next=ListNode(newVal,None)
            current=current.next
            
        if carry!=0:
            current.next=ListNode(carry,None)

        return head.next