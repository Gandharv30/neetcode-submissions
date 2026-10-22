class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        hashmap = {}
        for num in nums:
            hashmap[num]  = hashmap.get(num,0) + 1

        for num,cnt in hashmap.items():
            buckets[cnt].append(num)
        res = []
        
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                k-=1
                if k == 0 :
                    return res