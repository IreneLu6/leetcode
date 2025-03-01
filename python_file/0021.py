

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    p=list1
    q=list2
    if p==None :
        res=q
        return res
    if q==None :
        res=q
        return res
    if p.val<q.val:
        res=p
        tmp=p
        p=p.next
    else :
        res=q
        tmp=q
        q=q.next
    while(1):
        if p==None:
            tmp.next=q
            break
        elif q==None:
            tmp.next=p
            break
        elif p.val<q.val:
            tmp.next=p
            p=p.next
            tmp=tmp.next
        else:
            tmp.next=q
            q=q.next
            tmp=tmp.next
    return res


