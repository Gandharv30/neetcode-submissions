class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        max_len = 0
        n = len(s)
        seen = set()
        for right in range(n):
            #if s[right] in seen
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_len = max(max_len,len(seen))
        return max_len