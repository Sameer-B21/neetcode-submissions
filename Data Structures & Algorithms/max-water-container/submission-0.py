class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0, len(heights)-1
        t = 0
        while i < j:
            h = min(heights[i], heights[j])
            w = j - i
            t = max(t, h*w)
            if h == heights[i]:
                i+=1
            else:
                j-=1
        return t


        