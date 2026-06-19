class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        postfix = 1
        output = [1] * len(nums)
        output[0] = prefix
        for indx in range(len(nums)):
            output[indx] = prefix
            prefix = prefix * nums[indx]

        for ind in range(len(nums)-1,-1,-1):
            output[ind] *= postfix
            postfix *= nums[ind]

        return output
            
            


        
         
        