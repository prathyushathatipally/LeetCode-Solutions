# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        previous=None
        fast=head
        slow=head
        for i in range(n):
            if fast is None:
                return None
            fast=fast.next
        while fast is not None:
            previous=slow
            slow=slow.next
            fast=fast.next
        if previous is None:
            return head.next

        previous.next=slow.next
        return head

        