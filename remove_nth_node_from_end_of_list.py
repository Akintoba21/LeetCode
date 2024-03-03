# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tail = head
        c = 0
        while(tail != None):
            c = c + 1
            tail = tail.next
        rhead = ListNode()
        rtail = rhead
        for _ in range(c-n):
            rtail.next = head
            rtail = rtail.next
            head = head.next if head else None
        head = head.next if head else None
        rtail.next = head
        rhead = rhead.next
        return rhead