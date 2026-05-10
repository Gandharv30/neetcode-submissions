from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #time = distance/speed
        speed = sorted([(i,j,(target-i)/j) for i,j in zip(position,speed)],key= lambda x:x[0],reverse=True)
        stack = []
        for val in speed:
            stack.append(val[2])
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)