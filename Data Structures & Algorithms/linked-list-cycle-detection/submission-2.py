# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        single = head
        double = head

        while single and single.next and double and double.next and double.next.next:
            single = single.next
            double = double.next.next
            if single == double:
                return True
        return False