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
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.merge2Lists(l1, l2))
            lists = merged_lists
        return lists[0]
    
    def merge2Lists(self, l1:ListNode, l2:ListNode) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
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
