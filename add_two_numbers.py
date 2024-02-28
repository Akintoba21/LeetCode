# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rhead = ListNode()
        tail = rhead
        carry = 0
        while (l1 != None or l2 != None or carry != 0):
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            sum = n1 + n2 + carry
            digit = sum %10
            carry = sum // 10
            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        r = rhead.next
        rhead.next = None
        return r