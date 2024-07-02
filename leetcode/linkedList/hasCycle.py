def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen=set()

        while head!=None and head not in seen:
            seen.add(head)
            head=head.next
        return head!=None