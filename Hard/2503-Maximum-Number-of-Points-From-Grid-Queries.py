class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        d = {}
        arr = queries.copy()
        arr.sort()
        start = 0
        for i in range(len(arr)):
            if arr[i] > grid[0][0]:
                start = i
                break
            d[arr[i]] = 0
        row = len(grid)
        col = len(grid[0])
        heap = []
        heapq.heappush(heap,(grid[0][0],0,0))
        visit = set()
        visit.add((0,0))
        step = 0
        dirk = [(1,0),(0,1),(-1,0),(0,-1)]
        while start < len(arr):
            k = arr[start]
            while heap and k > heap[0][0]:
                v,i,j = heapq.heappop(heap)
                step += 1
                for r,c in dirk:
                    nr,nc = i+r,j+c
                    if 0 <= nr < row and 0 <= nc < col and (nr,nc) not in visit:
                        heapq.heappush(heap,(grid[nr][nc],nr,nc))
                        visit.add((nr,nc))

            d[arr[start]] = step
            start += 1
        res = []
        for i in queries:
            res.append(d[i])
        return res
