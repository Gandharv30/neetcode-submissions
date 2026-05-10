from typing import List
class Solution:
    def quick_sort(self,nums):
        if len(nums) < 1:
            return []
        pivot = nums[-1]
        left_arr = [x for x in nums[:-1] if x <= pivot]
        right_arr = [x for x in nums[:-1] if x > pivot]
        left_arr = self.quick_sort(left_arr)
        right_arr = self.quick_sort(right_arr)

        return left_arr + [pivot] + right_arr
    
    def merge_sort(self,nums):
        if len(nums) == 1:
            return nums
        
        mid = len(nums)//2
        left_arr = self.merge_sort(nums[:mid])
        right_arr = self.merge_sort(nums[mid:])
        len_l =  len(left_arr)
        len_r =  len(right_arr)

        ans = [0] * len(nums)
        i = 0
        l = 0
        r = 0
        while (l < len_l)  &  (r < len_r):
            if left_arr[l] > right_arr[r] :
                ans[i] = right_arr[r]
                r+=1
                
            else:
                ans[i] = left_arr[l]
                l+=1
            i+=1

        while l < len_l:
            ans[i] = left_arr[l]
            l+=1
            i+=1

        while r <  len_r:
            ans[i] = right_arr[r]
            r+=1
            i+=1

        return ans 

               
    def sortArray(self, nums: List[int]) -> List[int]:

        return self.merge_sort(nums=nums)




obj = Solution()
print(obj.sortArray([5,2,3,1])) 
        