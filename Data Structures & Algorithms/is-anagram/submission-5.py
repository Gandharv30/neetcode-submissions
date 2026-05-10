class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for val in s:
            hash_map[val] = hash_map.get(val,0) + 1
        hash_map_2 = {}
        for val in t:
            hash_map_2[val] = hash_map_2.get(val,0) + 1
         
        if len(hash_map) != len(hash_map_2):
            return False
        
        for val in s:
            val_in_s = hash_map.get(val,0)
            val_in_t = hash_map_2.get(val,0)
            if val_in_s == val_in_t:
                continue
            else:
                return False
        return True
        

   