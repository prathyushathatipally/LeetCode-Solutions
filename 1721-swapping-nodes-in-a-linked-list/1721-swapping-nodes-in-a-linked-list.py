# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        current=head
        c=0
        while current is not None:
            c+=1
            current=current.next
        first=head
        for i in range(k-1):
            first=first.next
        second=head
        for i in range(c-k):
            second=second.next
        first.val,second.val=second.val,first.val
        return head


        