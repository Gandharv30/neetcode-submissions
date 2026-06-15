class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # len(weights) = days  -- lower bound 
        #min weight capacity has to be max of weights 
        # max capacity can be total sum so total
        l = max(weights)
        r = sum(weights)
        ans = r

        def can_ship(cap):
            days_taken,currCap = 1,cap
            for w in weights:
                if currCap - w < 0:
                    days_taken += 1
                    currCap = cap
                currCap = currCap - w
            return days_taken <= days
                
        

        while l <= r :
            mid = (l+r) // 2 
            current_capacity = 0
            if can_ship(mid):
                ans = min(ans,mid)
                r = mid - 1
            else:
                l = mid+1
        return ans
