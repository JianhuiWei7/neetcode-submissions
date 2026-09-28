# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        pointer = dummy
        head1 = list1
        head2 = list2
        while head1 or head2:
            if head1 and head2:
                if head1.val > head2.val:
                    pointer.next = head2
                    head2 = head2.next
                    pointer = pointer.next
                else:
                    pointer.next = head1
                    head1 = head1.next
                    pointer = pointer.next
            elif head1:
                pointer.next = head1
                head1 = head1.next
                pointer = pointer.next
            else:
                pointer.next = head2
                head2 = head2.next
                pointer = pointer.next
        return dummy.next


        