class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        res = res = [[] for _ in range(len(nums) + 1)]
        ans = [] 

        for ele in nums:
            hash_map[ele] = hash_map.get(ele,0) + 1
            # get occurences


        for key,v in hash_map.items():
            indx = hash_map[key]
            res[indx].append(key)
        
        for ele in reversed(res):
            for num in ele:
                ans.append(num)
                if len(ans) == k:
                    return ans
    