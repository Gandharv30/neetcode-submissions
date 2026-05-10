from collections import defaultdict


class Solution:
    def get_char_to_replace(self,mapping):
        min_key = min(mapping, key=mapping.get)        # 'b'
        min_value = mapping[min_key] 
        return min_key,min_value

    def characterReplacement(self, s: str, k: int) -> int:
        count = 0 # count of character
        kv_store = defaultdict(int)
        max_len = 0
        max_freq = 0
        l = 0
        replace_count = 0
        # create dictionary of chars to decide which char needs to be replaced. 
        # The one which occurs least number of tik

        for r in range(len(s)):
            kv_store[s[r]] += 1
            max_freq = max(max_freq,kv_store[s[r]])

            # Shrink window condition ?
            # Shrink window when char is not in kv_store 
            while r - l + 1 - max_freq > k:
                kv_store[s[l]] -= 1
                l+=1


            current_len = r - l + 1
            max_len = max(max_len,current_len)
        return max_len
    
# obj = Solution()
# print(obj.characterReplacement(s = "AABABBA", k = 1))



