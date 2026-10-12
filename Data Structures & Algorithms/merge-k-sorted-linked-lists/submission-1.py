# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        dummy = ListNode()
        pointer = dummy
        heap = []
    
        for i in range(n):
            current_list = lists[i]
            if current_list:
                heapq.heappush(heap, (current_list.val, i))
        while heap:
            min_val, min_node_index = heapq.heappop(heap)
            pointer.next = lists[min_node_index]
            pointer = pointer.next
            lists[min_node_index] = lists[min_node_index].next
            if lists[min_node_index]:
                heapq.heappush(heap, (lists[min_node_index].val, min_node_index))
        return dummy.next









            
