class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    tmp1, tmp2 = l1, l2
    carry = 0
    head = None
    while tmp1 or tmp2:
        if tmp1 == None:
            val1 = 0
        else:
            val1 = tmp1.val
            tmp1 = tmp1.next
        if tmp2 == None:
            val2 = 0
        else:
            val2 = tmp2.val
            tmp2 = tmp2.next
        now = (val2 + val1 + carry) % 10
        carry = (val2 + val1 + carry) // 10
        if head == None:
            head = ListNode(now, None)
            tmp_Node = head
        else:
            tmp_Node.next = ListNode(now, None)
            tmp_Node = tmp_Node.next
    if carry!=0:
        tmp_Node.next = ListNode(carry, None)
        tmp_Node = tmp_Node.next
    return head

