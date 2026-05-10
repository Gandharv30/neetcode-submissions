# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         hash_map = {
#             ")":"(",
#             "}":"{",
#             "]":"["
#           }
        
#         for char in s :
#             if char not in hash_map:
#                 stack.append(char)
#             else:
#                 if stack and stack[-1] == hash_map[char]:
#                     stack.pop()
#                 else:
#                     return False
#         return True if not stack else False

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mapping = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        for bracket in s:
            if bracket not in  mapping:
                st.append(bracket)
            else:
                if st and st[-1] == mapping[bracket]:
                    st.pop()
                else:
                    return False
        return True if len(st) == 0 else False