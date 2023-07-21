  def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head.next
        slow=head
        fast=head.next.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        slow.next=slow.next.next
        return head
