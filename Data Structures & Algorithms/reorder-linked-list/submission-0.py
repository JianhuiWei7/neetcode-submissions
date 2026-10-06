# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_half_head = slow.next
        slow.next = None
        prev = None
        current = second_half_head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        second_half_head = prev
        pointer = head
        while pointer and second_half_head:
            pointer_next = pointer.next
            second_half_head_next = second_half_head.next
            pointer.next = second_half_head
            second_half_head.next = pointer_next
            pointer = pointer_next
            second_half_head = second_half_head_next




