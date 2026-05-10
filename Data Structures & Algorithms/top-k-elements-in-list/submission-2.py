from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for indx, val in enumerate(nums):
            hashmap[val] = hashmap.get(val,0) + 1
        
        count = [[] for i in range(len(nums)+1)]

        for key,val in hashmap.items():
            count[val].append(key)
        
        res = []
        for i in range(len(count) -1,0,-1):
            for val in count[i]:
                if k == 0:
                    break
                res.append(val)
                k-=1
        return res
