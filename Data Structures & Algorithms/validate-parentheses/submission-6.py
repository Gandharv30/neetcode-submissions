class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        st = []
        for char in s :
            if char in hash_map:
                if st and st[-1] == hash_map[char]:st.pop()
                else: return False

            else: st.append(char)
        return True if not st else False