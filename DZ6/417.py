class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit_set, prev_height):

            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                (r, c) in visit_set or
                heights[r][c] < prev_height):
                return

            visit_set.add((r, c))

            dfs(r + 1, c, visit_set, heights[r][c])
            dfs(r - 1, c, visit_set, heights[r][c])
            dfs(r, c + 1, visit_set, heights[r][c])
            dfs(r, c - 1, visit_set, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])

        return result
