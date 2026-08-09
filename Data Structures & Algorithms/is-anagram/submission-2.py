class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        temp = {}
        for c in s:
            temp[c] = temp.get(c,0)+1
        for c in t:
            if c not in temp or temp[c] == 0:
                return False
            temp[c]-=1
        return True

        