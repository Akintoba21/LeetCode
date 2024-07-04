# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = ListNode()
        rhead = r
        sum = 0
        while head:
            if head.val == 0:
                rhead.next = ListNode(sum)
                rhead = rhead.next
                sum = 0
            else:
                sum += head.val
            head = head.next
        r = r.next.next
        return r