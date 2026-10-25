class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        st = []
        ans = [0] * len(temperatures)
        for indx, temp in enumerate(temperatures):
            while st and st[-1][1] < temp:
                stind,sttemp = st.pop()
                ans[stind] = indx - stind
            st.append((indx,temp))
        return ans