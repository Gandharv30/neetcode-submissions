class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current path 
        visitng = set()

        def dfs(crs):
            if crs in visitng:
                return False
            if preMap[crs] == []:
                return True

            visitng.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False  

            visitng.remove(crs)
            preMap[crs] = []
            return True



        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


        