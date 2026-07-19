class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=[]
        for s in strs:
            encoded.append(str(len(s)) + "#" + s)
        return "".join(encoded)
        
            

    def decode(self, s: str) -> List[str]:
        new=[]
        i = 0 
        while i < len(s):

            j=i
            while s[j] != "#":
                j+=1

            l = int(s[i:j])

            word=s[j+1:j+1+l]

            new.append(word)

            i = j + l + 1
        
        return new

