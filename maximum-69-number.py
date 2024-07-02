class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        r = s.replace("6", "9", 1)
        return int(r)