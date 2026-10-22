
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        
        for ele in range(len(strs)):
            ans = [0] * 26
            for char in strs[ele]:
                ans[ord(char)  - ord('a')] += 1 

            hashmap[tuple(ans)].append(strs[ele])
        
        return list(hashmap.values())
        