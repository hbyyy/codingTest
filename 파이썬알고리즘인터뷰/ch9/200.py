from typing import List


class Solution:

    def dfs(self, v, visited, arr):
        x, y = v
        visited[x][y] = 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < self.n and 0 <= ny < self.m) and visited[nx][ny] == 0:
                if arr[nx][ny] == "1":
                    self.dfs((nx, ny), visited, arr)

    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        self.n, self.m = len(grid), len(grid[0])
        visited = [[0] * self.m for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    print(visited)
                    self.dfs((i, j), visited, grid)
                    answer += 1
        return answer


s = Solution()
s.numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
