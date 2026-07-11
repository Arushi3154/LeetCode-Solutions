# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break
                
            group_next = kth.next
            
            prev = group_next
            curr = group_prev.next
            
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            tmp = group_prev.next  # This was the old head, now it's the tail
            group_prev.next = kth  # 'kth' is now the new head of this group
            group_prev = tmp       # Move group_prev to the tail for the next iteration
            
        return dummy.next
    
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
