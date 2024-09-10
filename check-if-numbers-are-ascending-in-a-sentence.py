class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(" ")
        prev = None
        for x in s:
            try:
                temp = int(x)
                if prev and prev >= temp: return False
                prev = temp
            except:
                continue
        return True