# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current=head.next
        total=0
        dummy = ListNode(0)
        tail = dummy
        while current is not None:
            if current.val==0:
                new_node = ListNode(total)
                tail.next = new_node
                tail = tail.next

                total=0
            else:
                total+=current.val
            current=current.next
        return  dummy.next



            
        
        