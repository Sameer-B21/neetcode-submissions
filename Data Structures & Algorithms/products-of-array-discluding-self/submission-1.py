class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        r = []
        m = 1
        i = 0
        length = len(nums)
        while i < length:
            l.append(m)
            m*=nums[i]
            i+=1
        m = 1
        i = length-1
        while i >= 0:
            r.append(m)
            m*=nums[i]
            i-=1
        sol = []
        for i in range(length):
            sol.append(l[i]*r[-i-1])
        
        return(sol)