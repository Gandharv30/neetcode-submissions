class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ans = 0 
        for ele in tokens:
            if ele not in ('+','*','-','/'):
                st.append(int(ele))
            else:
                num1 = int(st.pop())
                num2 = int(st.pop())
                if ele == '+':
                    st.append(num1+num2)
                    # pass
                elif ele == '*':
                    st.append(num1*num2)
                elif ele == '-':
                    st.append(num2 - num1)
                elif ele == '/':
                    st.append(int(num2/num1))

        return st[-1]

                










    
    