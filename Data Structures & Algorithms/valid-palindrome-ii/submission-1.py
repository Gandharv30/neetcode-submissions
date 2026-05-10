class Solution:
    def isPalindrome(self,l,r,s):
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

    
    def validPalindrome(self, s: str) -> bool:
        """
        This solution takes extra space.
        """
        l,r = 0, len(s) - 1
        char_to_del = ""
        count = 0
        while l < r:
            if s[l]!=s[r]:
                skipL= self.isPalindrome(l+1,r,s)
                skipR=self.isPalindrome(l,r-1,s)
                return skipL or skipR
            l+=1
            r-=1
        return True
    