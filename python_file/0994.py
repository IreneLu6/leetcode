class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        fresh = 0
        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        def neighbors(r, c) -> (int, int):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        time = 0

        while queue and fresh > 0:
            q_len = len(queue)
            for i in range(q_len):
                r, c = queue.popleft()
                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            time += 1

        if fresh:
            return -1
        return time