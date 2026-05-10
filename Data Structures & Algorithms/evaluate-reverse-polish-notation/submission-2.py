class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[-1])
        st = []
        s2 = []
        div = "/"
        mul = "*"
        add = "+"
        sub = "-"
        for i in tokens:
            if i not in [div,mul,add,sub]:
                st.append(i)
            else :
                top = int(st.pop())
                next_top = int(st.pop())
                if i == div:
                    ans = next_top/top
                elif i == mul:
                    ans = next_top * top
                elif i == add: 
                    ans = next_top + top
                elif i == sub:
                    ans = next_top - top
                st.append(ans)
        return int(st.pop())