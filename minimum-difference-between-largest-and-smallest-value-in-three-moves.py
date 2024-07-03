class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        left = 0
        right = len(nums) - 1
        self.ans = nums[right] - nums[left]

        def recurse(l, r, count):
            if r <= l: return
            if count >= 3: return
            
            t1 = nums[r] - nums[l+1]
            t2 = nums[r-1] - nums[l]
            if t1 < t2:
                if t1 < self.ans: self.ans = t1
            elif t1 == t2:
                if t1 < self.ans: self.ans = t1
            else:
                if t2 < self.ans: self.ans = t2
            recurse(l+1, r, count+1)
            recurse(l, r-1, count+1)
            return

        recurse(left, right, 0)
        return self.ans