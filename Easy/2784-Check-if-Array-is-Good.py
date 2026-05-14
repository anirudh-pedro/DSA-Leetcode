class Solution:
    def isGood(self, nums: List[int]) -> bool:
        d = Counter(nums)
        if len(d) == len(nums) - 1:
            if min(d.keys()) == 1 and max(d.keys()) == len(nums) - 1 and d[max(nums)] == 2:
                return True
        return False
