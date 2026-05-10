class Solution:
    def check(self,s1,s2):
        if len(s1) != len(s2):
            return False
        else:
            for key,value in s1.items():
                
                if (not s2.get(key,None) is None) and (s1[key] == s2[key]):
                    continue
                else:
                    return False
        return True
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        for indx, val in enumerate(s):
            if s1.get(val,None) is None:
                s1[val] = 1
            else:
                s1[val] += 1
        for indx, val in enumerate(t):
            if s2.get(val,None) is None:
                s2[val] = 1
            else:
                s2[val] += 1
        return self.check(s1,s2)
        
            
