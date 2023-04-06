from ast import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        cycle, taken = set(), set()

        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in taken:
                # do nothing because we don't need to take the course again
                return True

            # a course has 3 possible states:
            # taken -> crs has been added to res
            # taking -> crs not added to res, but added to cycle
            # not taken -> crs not added to output or cycle
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            taken.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res
