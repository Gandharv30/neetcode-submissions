class Solution:

    def encode(self, strs: List[str]) -> str:

        spl_char = "#"
        res = ""
        for indx,val in enumerate(strs):
            size = len(val)
            res += str(size)+"#"+val
        return res

    def decode(self, s: str) -> List[str]:

        
        i =0
        res = []
        while i < len(s):
            j = i
            size = ""
            while s[j]!= "#":
                j += 1
            size = int(s[i:j])
            res.append( s[j+1 : j+size+1])
            i = j+size+1
            

        return res
