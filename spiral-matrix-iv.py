# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        r = [[-1] * n for _ in range(m)]
        x, y, d = 0, 0, 0
        while head:
            r[x][y] = head.val
            if d == 0:
                if y < n-1 and r[x][y+1] == -1:
                    y += 1
                else:
                    d = 1
                    x += 1
            elif d == 1:
                if x < m-1 and r[x+1][y] == -1:
                    x += 1
                else:
                    d = 2
                    y -= 1
            elif d == 2:
                if y > 0 and r[x][y-1] == -1:
                    y -= 1
                else:
                    d = 3
                    x -= 1
            elif d == 3:
                if x > 0 and r[x-1][y] == -1:
                    x -= 1
                else:
                    d = 0
                    y += 1
            head = head.next
        return r