class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0]
        maxR = [0]
        t = 0
        for i in range(1, len(height)):
            if t < height[i-1]:
                t = height[i-1]
            maxL.append(t)
        t = 0
        for i in range(len(height)-2, -1, -1):
            if t < height[i+1]:
                t = height[i+1]
            maxR.append(t)


        count = 0
        for i in range(len(height)):
            c = min(maxL[i], maxR[-i]) - height[i]
            if c > 0:
                count+= c

        return count


        