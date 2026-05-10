class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(int(stack[-1])*2)
            elif i == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))
    
            else:
                stack.append(int(i))
        ans = 0
        for i in stack:
            ans+=i

        return ans