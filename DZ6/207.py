class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visitSet = set()


        def dfs(crs):

            if crs in visitSet:
                return False

            if adj[crs] == []:
                return True

            visitSet.add(crs)

            for pre in adj[crs]:
                if not dfs(pre):
                    return False

            visitSet.remove(crs)

            adj[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
