class Solution:
    def _reverse(self,nums,start,end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1
        return nums
    
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums = self._reverse(nums=nums,start=0,end=len(nums)-1)
        nums = self._reverse(nums=nums,start=0,end=k-1)
        nums = self._reverse(nums=nums,start=k,end=len(nums)-1)
        