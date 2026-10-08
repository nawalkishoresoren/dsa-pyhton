# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head:ListNode)->ListNode:
        prev, curr = None, head
        while curr:
            nxt_node = curr.next
            curr.next = prev
            prev = curr
            curr = nxt_node
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        mid, fast = head, head.next

        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        first = head
        second = mid.next
        mid.next = None
        second = self.reverse(second)

        while second:
            nxt_first, nxt_second = first.next, second.next
            first.next = second
            second.next = nxt_first
            first = nxt_first
            second = nxt_second
        