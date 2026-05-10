from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for char in s1:
            d1[char]+=1
        l = 0
        r = len(s1)

        # check in first window
        s2_ = s2[l:r]
        for char in s2_:
            d2[char]+=1
        if d1==d2:
            return True
        while r < len(s2):
            d2[s2[l]]-=1
            if d2[s2[l]] <=0:
                del d2[s2[l]]
            d2[s2[r]]+=1
            l+=1
            r+=1
            if d2==d1:
                return True
        return False