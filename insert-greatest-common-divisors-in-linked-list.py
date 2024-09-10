# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            temp = cur.next
            cur.next = ListNode(gcd(cur.val, temp.val))
            cur = cur.next
            cur.next = temp
            cur = cur.next
        return head