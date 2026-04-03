# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        p1, p2 = l1, l2
        dummy = ListNode()
        n = dummy
        while p1 or p2 or carry_over > 0:
            temp1, temp2 = 0, 0
            # Set P1
            if p1:
                temp1 = p1.val
                p1 = p1.next
            else:
                temp1 = 0
            
            # Set P2
            if p2:
                temp2 = p2.val
                p2 = p2.next
            else:
                temp2 = 0
            
            # calculate
            s = temp1 + temp2 + carry_over
            carry_over = s // 10
            n.next = ListNode(s % 10)
            n = n.next
        
        return dummy.next