class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}
        for val in s:
            hash_map_s[val] = hash_map_s.get(val,0) + 1 
        for val in t:
            hash_map_t[val] = hash_map_t.get(val,0) + 1

        # check if two hash_maps are identical
        key_1 = hash_map_s.keys()
        key_2 = hash_map_t.keys()
        if len(key_1) != len(key_2):
            return False
        final = hash_map_s if len(key_1) >= len(key_2) else hash_map_t

        for k,v in final.items():
            val_in_t = hash_map_t.get(k,0)
            if val_in_t != v:
                return False
        return True

        

   