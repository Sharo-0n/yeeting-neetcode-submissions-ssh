# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O( n log k )
        if len(lists) == 0:
            return None
        while len(lists) > 2:
            new_list = self.merge2Lists(lists[len(lists)-1], lists[len(lists)-2])
            del lists[len(lists)-1]
            lists[len(lists)-1] = new_list
        if len(lists) == 2:
            return self.merge2Lists(lists[0], lists[1])
        else:
            return lists[0]
    
    def merge2Lists(self, l1:ListNode, l2:ListNode) -> Optional[ListNode]:
        head = None
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        curr = head
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        
        curr = head
        while curr.next:
            curr = curr.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        return head
