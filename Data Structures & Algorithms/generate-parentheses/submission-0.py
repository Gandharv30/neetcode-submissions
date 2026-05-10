class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []
        def backtrack(openC,closeC):
            if n == openC == closeC:
                res.append("".join(sol))
                return
            if openC < n :
                sol.append("(")
                backtrack(openC+1,closeC)
                sol.pop()

            if closeC < openC:
                sol.append(")")
                backtrack(openC,closeC+1)
                sol.pop()
            
        backtrack(0,0)

        return res
        