# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s=set(nums)
        while head and head.val in s:
            head=head.next
        current=head
        while current is not None and current.next is not None:
            if current.next.val in s:
                current.next=current.next.next
            else:
                current=current.next
        return head

            

        