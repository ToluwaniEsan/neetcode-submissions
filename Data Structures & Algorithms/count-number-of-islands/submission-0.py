class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        '''
        Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],   [1,0]
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
         
        '''

        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(i, j):
            
            stack = [(i, j)]

            while stack:
                x, y = stack.pop()

                if (x, y) in visited:
                    continue
                visited.add((x, y))

                for r, c in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == '1':
                        stack.append((r,c))

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1

        return islands


