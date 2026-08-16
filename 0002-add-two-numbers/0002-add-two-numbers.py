# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        current=dummy
        total=0
        carry=0
        digit=0
        while l1 is not None or l2 is not None:
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0
            total=a+b+carry
            digits=total%10
            carry=total//10
            current.next=ListNode(digits)
            current=current.next
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        if carry:
            current.next=ListNode(carry)
        return dummy.next


        