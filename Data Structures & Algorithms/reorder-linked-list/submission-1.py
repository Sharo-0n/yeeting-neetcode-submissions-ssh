class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        mdpt = head
        end = head
        while end and end.next:
            end = end.next.next
            mdpt = mdpt.next

        # reverse second half (excluding midpoint from first half)
        second_half_head = mdpt.next
        mdpt.next = None
        prev = None
        curr = second_half_head
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        second_half_head = prev

        insert = second_half_head
        main = head
        while insert:
            main_next_temp = main.next
            insert_next_temp = insert.next
            main.next = insert
            insert.next = main_next_temp
            main = main_next_temp
            insert = insert_next_temp