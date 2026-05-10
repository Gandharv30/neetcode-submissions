from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        hashMap = defaultdict(list)
        for words in strs:
            count = [0]*26
            for chars in words:
                count[ord(chars)-ord('a')] += 1
            count = tuple(count)
            hashMap[count].append(words)
        return  list(hashMap.values())

        