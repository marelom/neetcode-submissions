# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        index = {}
        curr = head
        while curr:
            node = curr
            index[node] = True
            next_node = curr.next
            if next_node in index:
                return True
            elif next_node == None:
                return False
            curr = curr.next     
        return curr
                  
