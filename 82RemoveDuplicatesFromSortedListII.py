class Solution:  
    # @param head, a ListNode  
    # @return a ListNode  
    def deleteDuplicates(self, head):  
        if not head or not head.next:
            return head
        dummy = prev = ListNode(0)
        while head and head.next:
            if head.val == head.next.val:
                val = head.val
                while head and head.val == val:
                    head = head.next
                prev.next = head  ######
            else:
                prev.next = head
                prev = prev.next
                head = head.next
        return dummy.next
