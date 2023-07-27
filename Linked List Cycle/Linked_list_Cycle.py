#Hashmap
def hasCycle(self, head: Optional[ListNode]) -> bool:
  dict={}
  while head:
    if head in dict:
      return True
    dict[head]=True
  return False


#Tortoise and hare
slow=fast=head
while(fast and fast.next):
  slow=slow.next
  fast=fast.next.next
  if(slow==fast):
    return True
return False
  
