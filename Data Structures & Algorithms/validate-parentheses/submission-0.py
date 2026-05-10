class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {
            ")":"(",
            "}":"{",
            "]":"["
          }
        
        for char in s :
            if char not in hash_map:
                stack.append(char)
            else:
                if stack and stack[-1] == hash_map[char]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False