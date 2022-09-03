from typing import (
    List,
)
from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS, COLS, DIRS = len(rooms), len(rooms[0]), [[-1,0],[0,-1],[1,0],[0,1]]
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if not rooms[r][c]:
                    for dr, dc in DIRS:
                        q.append([r + dr, c + dc])
        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                rooms[r][c] <= dist):
                    continue
                rooms[r][c] = dist
                for dr, dc in DIRS:
                    q.append([r + dr, c + dc])
            dist += 1
