class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        FRESH = 1
        ROTTEN = 2
        q = collections.deque()
        fruit = 0
        time = 0
        directions = [
            (1,0),
            (-1,0),
            (0,-1),
            (0,1)
        ]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == FRESH:
                    fruit += 1

                elif grid[r][c] == ROTTEN:
                    q.append((r,c))
        

        while q and fruit > 0:
            length = len(q)
            for _ in range(length):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col =  dr+r,dc+c
                    if (0 <= row < ROWS) and (0 <= col < COLS) and grid[row][col] == 1:
                        grid[row][col]  = 2 # set to ROTTEN
                        q.append((row,col))
                        fruit -=1 

            
            
            time+=1
        return time if fruit == 0 else -1 








