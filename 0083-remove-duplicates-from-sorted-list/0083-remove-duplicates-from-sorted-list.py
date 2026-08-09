# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        seen=set()
        current=head
        previous=None
        while current:
            if current.val not in seen:
                seen.add(current.val)
                previous=current
            else:
                previous.next=current.next
            current=current.next
        return head

        
        