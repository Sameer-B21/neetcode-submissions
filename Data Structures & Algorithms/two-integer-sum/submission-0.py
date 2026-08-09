class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in t:
                return [t[n], i]
            t[nums[i]] = i