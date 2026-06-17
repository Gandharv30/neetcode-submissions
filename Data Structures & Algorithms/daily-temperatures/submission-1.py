class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        st = []
        res = [0] * len(temperatures) 

        for indx,temp in enumerate(temperatures):

            while st and st[-1][1] < temp:
                ind,tmp = st.pop()
                res[ind] = indx - ind
            st.append((indx,temp))
        return res
