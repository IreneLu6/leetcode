from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs( head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(head)
    p, t, q = dummy, head, head.next
    if q == None:
        return head

    while q!=None and q.next != None:
        p.next = q
        p.next = q.next
        q.next = t
        p, t, q = t, p.next, p.next.next

    p.next = q
    p.next = q.next
    q.next = t

    return dummy.next

e = ListNode(5)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

swapPairs(a)

