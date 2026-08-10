# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        current=head
        previous=None
        while current is not None:
            if current.val==val:
                if previous is None:
                    head=current.next
                else:
                    previous.next=current.next
            else:
                previous=current
            current=current.next
        return head
                
                
        