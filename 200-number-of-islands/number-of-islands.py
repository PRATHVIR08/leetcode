class Solution:
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])

        # Check boundaries and water cells
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return

        # Mark current land as visited
        grid[i][j] = '0'

        # Visit all four directions
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)

        return count


# Driver Code
grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]

obj = Solution()
print("Number of Islands:", obj.numIslands(grid))