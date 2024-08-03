class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        for x in range(len(arr)):
            if arr[x] != target[x]:
                return False
        return True