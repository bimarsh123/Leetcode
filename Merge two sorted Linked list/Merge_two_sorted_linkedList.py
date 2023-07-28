#Two pointer approach
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  dummy=ListNode()
  last=dummy
  while list1 and list2:
    if(list1.data<list2.data):
      last.next=list1
      list1=list1.next
    else:
      last.next=list2
      list2=list2.next
  if(list1):
    last.next=list1
  else:
    last.next=list2
  return dummy.next


#Recursion
 def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
   if(list1!=None):
     return list2
    if(list2!=None):
      return list1
    if(list1.data<list2.data):
      list1.next=self.mergeTwoLists(list1.next,list2)
    else:
      list2.next=self.mergeTwoLists(list1,list2.next)
    
