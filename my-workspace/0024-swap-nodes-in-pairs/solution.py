# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node pointing to the head
        dummy = ListNode(0, head)
        prev = dummy
        
        # We need at least two nodes ahead to perform a swap
        while prev.next and prev.next.next:
            # Identify the two nodes to swap
            first = prev.next
            second = first.next
            
            # Change the pointers to perform the swap
            first.next = second.next  # Link first node to the rest of the list
            second.next = first       # Put first node behind second node
            prev.next = second        # Link previous section to the new pair head
            
            # Move 'prev' two steps forward (to the tail of the swapped pair)
            prev = first
            
        return dummy.next
