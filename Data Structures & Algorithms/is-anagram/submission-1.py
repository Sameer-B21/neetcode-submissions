class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        temp = {s:[0]*26, t:[0]*26}
        for i in range(len(s)):
            temp[s][ord(s[i]) - ord('a')] += 1
            temp[t][ord(t[i]) - ord('a')] += 1
        if temp[s] != temp[t]:
            return False
        return True

        