class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, h = i+1, len(nums)-1
            while l<h:
                total = nums[i] + nums[l] + nums[h]
                if total == 0:
                    if [nums[i], nums[l], nums[h]] not in arr:
                        arr.append([nums[i], nums[l], nums[h]])
                    l+=1
                    h-=1
                elif total < 0:
                    l+=1
                else:
                    h-=1
        return arr
