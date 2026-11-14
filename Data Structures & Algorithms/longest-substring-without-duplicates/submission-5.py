class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0 
        res =0
        freq_map = {}

        while r < len(s):
            if s[r] in freq_map:
                l = max(freq_map[s[r]]+1,l)
            freq_map[s[r]] = r 
            res = max(r-l+1,res)
            r+=1
        return res
