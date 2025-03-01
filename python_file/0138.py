"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            head2 = None
            return head2
        if head.next == None:
            head2 = Node(head.val)
            if head.random:
                head2.random = head2
            return head2

        # 创建一个映射表，用于存储原节点和新节点的对应关系
        point_dict = {}
        head2 = Node(head.val)  # 创建新链表的头节点
        p = head2
        tmp = head.next

        # 遍历原链表，创建新节点并建立映射关系
        while tmp:
            q = Node(tmp.val)  # 创建新节点
            p.next = q  # 连接新链表
            p = p.next
            point_dict[tmp] = q  # 建立映射关系
            tmp = tmp.next


        # 处理头节点的 random 指针
        point_dict[head] = head2
        if head.random:
            head2.random = point_dict[head.random]

        tmp1 = head
        tmp2 = head2
        while tmp1:
            if tmp1.random != None:
                tmp2.random = point_dict[tmp1.random]
            tmp1, tmp2 = tmp1.next, tmp2.next

        return head2