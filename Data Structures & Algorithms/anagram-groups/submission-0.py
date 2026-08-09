class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for s in strs:
            c = [0] * 26
            for i in s:
                c[ord(i) - ord('a')]+=1
            p = tuple(c)
            temp.setdefault(p,[]).append(s)
        return (list(temp.values()))