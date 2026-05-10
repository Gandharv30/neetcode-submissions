class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans= [0] * len(nums)
        l,r = 1,1
        left_arr = [0]* len(nums)
        right_arr = [0] * len(nums)

        for i in range(len(nums)):
            j = -i -1 # traverse array for back 
            left_arr[i]  = l
            right_arr[j] = r
            l  *= nums[i]
            r *= nums[j]
        return [i*j for i,j in zip(left_arr,right_arr)]