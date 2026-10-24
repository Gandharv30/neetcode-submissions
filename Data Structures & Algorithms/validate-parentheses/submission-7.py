class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        

        st = []
        for char in s:
            if char in mapping:
                if st and st[-1] == mapping[char]:
                    st.pop()
                else:
                    return False
            else:
                st.append(char)
        return True if not st else False