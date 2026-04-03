# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        dummy.next = curr
        carry = 0
        
        while l1 or l2 or carry > 0:
            temp1, temp2 = 0,0
            curr.next = ListNode()
            curr = curr.next
            if l1:
                temp1 = l1.val
                l1 = l1.next

            if l2:
                temp2 = l2.val
                l2 = l2.next

            s = temp1 + temp2 + carry
            curr.val = s % 10             
            carry = s // 10
            

        return dummy.next