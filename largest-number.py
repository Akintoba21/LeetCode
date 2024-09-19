from functools import cmp_to_key

class Solution:
    def cmp(self, a,b):
        if a+b > b+a:
            return -1
        if a+b==b+a:
            return 0
        else:
            return 1

    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        nums.sort(key=cmp_to_key(self.cmp))
        return str(int("".join(nums)))
                