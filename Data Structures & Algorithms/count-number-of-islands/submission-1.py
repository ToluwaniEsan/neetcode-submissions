class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()#this is where I will store the islands I have visited

        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            #note: DFS uses a stack, BFS uses a Queue
            stack = [(i, j)]

            while stack:
                i, j = stack.pop()
                if (i, j) in visited:
                    continue
                visited.add((i, j))

                for r, c in [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]:
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == "1":
                        stack.append((r, c))

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1
        return islands

