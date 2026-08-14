class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        temp = sorted(nums)
        count = 0
        t = 1
        for i in range(len(nums)-1):
            if temp[i] == temp[i+1]:
                continue
            if temp[i+1] == temp[i] + 1:
                t+=1
            else:
                if t > count:
                    count = t
                t = 1
        if t > count:
            count = t
        return count
