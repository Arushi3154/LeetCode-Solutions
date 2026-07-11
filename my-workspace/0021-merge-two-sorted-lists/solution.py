# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the starting anchor
        dummy = ListNode(-1)
        # 'current' will move along as we build the new list
        current = dummy
        
        # Loop while both lists still have nodes to compare
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next  # Move list1 pointer forward
            else:
                current.next = list2
                list2 = list2.next  # Move list2 pointer forward
                
            current = current.next  # Move our merged list pointer forward
            
        # If one list runs out, wire up the rest of the remaining list
        current.next = list1 if list1 else list2
        
        # The actual head of the merged list is right after the dummy node
        return dummy.next
