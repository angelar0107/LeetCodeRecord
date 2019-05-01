# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head
        length = n - m + 1
        while  m - 1 :
            pre, head = pre.next, head.next
            m -= 1
        newtail, newhead = head, None 
        while length:
            head.next,newhead,head = newhead,head,head.next
            length -= 1
        newtail.next = head
        pre.next = newhead
        return dummy.next
                
