class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min_rate = 1
        # max_rate  = max(piles)
        # rate lies between 1 and max(piles)
        # apply binary search between one to (max_piles) to get h
        if h == len(piles):
            return max(piles)

        l = 1 
        r = max(piles)
        res = 0

        while l <= r:
            hours = 0
            mid = (l+r) // 2 
            for p in piles:
                hours += math.ceil(p/mid)
            if hours <= h:
                res = mid
                r = mid - 1         
            else:
                l = mid + 1
        return res
                
            


        