class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head

    tmp,tmp_n=dummy,dummy
    for i in range(n + 1):
        tmp = tmp.next
    while tmp!=None:
        tmp=tmp.next
        tmp_n=tmp_n.next
    tmp_n.next=tmp_n.next.next
    return dummy.next