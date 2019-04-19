# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        length = 0
        traverse = head
        while traverse:
            traverse = traverse.next
            length += 1
        k = k % length
        if not k:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        result = slow.next
        fast.next = head
        slow.next = None
        return result
