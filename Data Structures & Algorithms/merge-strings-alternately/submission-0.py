class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i = 0
        total_len = len(word1) + len(word2)

        while i < total_len :
            if i >= len(word1) and i>= len(word2):
                return ans
            res = ""
            if i < len(word1) and i <  len(word2):
                res  += word1[i] + word2[i]
            
            elif i >= len(word1) and i < len(word2):
                res  = word2[i]

            else:
                res = word1[i]
            
            ans += res
            i+=1

        return ans