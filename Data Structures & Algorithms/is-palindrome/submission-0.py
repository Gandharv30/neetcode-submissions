class Solution:

    def isAlphaNumberic(self, c):
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))
        
        

    def isPalindrome(self, s: str) -> bool:
        lower_case_start = ord('a')
        lower_case_end = ord('z')
        upper_case_start = ord('A')
        upper_case_end = ord('Z')
        l = 0
        r = len(s) - 1     

        while l < r :
            # Increase counter if its outside of the range
            while l < r and not self.isAlphaNumberic(s[l]):
                l+=1
            
            while r > l and not self.isAlphaNumberic(s[r]):
                r-=1
            
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False

        return True