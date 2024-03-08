# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = head
        count = 0
        while(tail.next):
            tail = tail.next
            count = count + 1
        half = -(count // -2)
        for _ in range(half):
            head = head.next
        return head