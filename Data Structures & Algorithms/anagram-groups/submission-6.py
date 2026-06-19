class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = defaultdict(list)
        for val in strs:
            res =[0] * 26

            for char in val:
                res[ord(char) - ord('a')] += 1
            hash_map[tuple(res)].append(val)
        return list(hash_map.values())
        