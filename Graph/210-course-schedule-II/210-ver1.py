from ast import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # does not work if there is a cycle
        res = []
        taken = set()

        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs, res):
            if crs in taken:
                return
            if preMap[crs] == [] and crs not in res:
                res.append(crs)
                return

            taken.add(crs)
            for pre in preMap[crs]:
                dfs(pre, res)
            taken.remove(crs)
            preMap[crs] = []
            if crs not in res:
                res.append(crs)

        for crs in range(numCourses):
            dfs(crs, res)
        return res
