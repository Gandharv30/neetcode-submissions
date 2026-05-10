class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans  = nums[0]
        st, end = 0 , len(nums) - 1
        while st <= end:
            if nums[st] < nums[end]:
                ans = min(ans,nums[st])
                break
            mid = st + (end-st)//2
            ans =min(ans,nums[mid])
            #right array
            if nums[st] <= nums[mid]:
                st = mid + 1
            #right array
            else:
                end = mid - 1
            

        return ans
        