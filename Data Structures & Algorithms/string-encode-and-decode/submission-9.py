class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string = encoded_string + str(len(s)) + "#" + s
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            jump = int(s[i:j])
            start = j+1
            i = start+jump
            decoded_strs.append(s[start:i])      
        return decoded_strs