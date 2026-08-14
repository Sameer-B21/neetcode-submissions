class Solution:
    def isPalindrome(self, s: str) -> bool:
        alp = 'abcdefghijklmnopqrstuvwxyz0123456789'
        temp = s.lower()
        i, j = 0, len(temp)-1
        while i<=j:
            if temp[i] not in alp:
                i+=1
                continue
            if temp[j] not in alp:
                j-=1
                continue
            if temp[i]!=temp[j]:
                return False
            i+=1
            j-=1
        return True
        