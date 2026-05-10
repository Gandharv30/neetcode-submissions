from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for indx, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        ans = []
        for key,val in hashmap.items():
            ans.append([key,val])
        ans = sorted(ans,key = lambda x:x[1])
        for indx,ele in enumerate(ans):
            ans[indx] = ans[indx][0]
        return ans[::-1][:k]