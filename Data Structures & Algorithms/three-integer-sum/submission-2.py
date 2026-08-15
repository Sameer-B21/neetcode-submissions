class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        numbers = sorted(nums)
        for i in range(len(numbers)):
            l, h = i+1, len(numbers)-1
            while l<h:
                total = numbers[i] + numbers[l] + numbers[h]
                if total == 0:
                    if [numbers[i], numbers[l], numbers[h]] not in arr:
                        arr.append([numbers[i], numbers[l], numbers[h]])
                    l+=1
                    h-=1
                elif total < 0:
                    l+=1
                else:
                    h-=1
        return arr
