# 417. Pacific Atlantic Water Flow

**Difficulty:** Medium  
**Topics:** Array, Depth-First Search, Breadth-First Search, Matrix  
**Companies:** Google, Amazon, Microsoft

## Problem Description

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The Pacific Ocean touches the island's **left and top edges**, and the Atlantic Ocean touches the island's **right and bottom edges**.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can **flow to neighboring cells** directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a **2D list of grid coordinates** `result` where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to **both the Pacific and Atlantic oceans**.

## Examples

### Example 1:

```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
```

### Example 2:

```
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
```

## Constraints

- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`

## Solution

```python
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        # Sets to track cells that can reach each ocean
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable_set, prev_height):
            """
            DFS to mark all cells reachable from current cell.
            Water flows from higher to lower or equal height.
            """
            # Base cases: out of bounds, already visited, or can't flow here
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in reachable_set or prev_height > heights[r][c]):
                return

            # Mark current cell as reachable
            reachable_set.add((r, c))

            # Explore all 4 directions with current height as previous
            current_height = heights[r][c]
            dfs(r + 1, c, reachable_set, current_height)  # Down
            dfs(r - 1, c, reachable_set, current_height)  # Up
            dfs(r, c + 1, reachable_set, current_height)  # Right
            dfs(r, c - 1, reachable_set, current_height)  # Left

        # Start DFS from all Pacific Ocean borders (top and left edges)
        for col in range(cols):
            dfs(0, col, pacific_reachable, heights[0][col])          # Top edge
            dfs(rows-1, col, atlantic_reachable, heights[rows-1][col])  # Bottom edge

        for row in range(rows):
            dfs(row, 0, pacific_reachable, heights[row][0])          # Left edge
            dfs(row, cols-1, atlantic_reachable, heights[row][cols-1])  # Right edge

        # Find intersection: cells reachable by both oceans
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])

        return result
```

## Algorithm Explanation

This solution uses **reverse flow DFS** from ocean borders:

### Key Insight

- Instead of checking if each cell can reach both oceans (expensive)
- Start from ocean borders and find all cells that can flow **to** each ocean
- **Reverse the flow direction**: if water flows from A to B, then B is reachable from A

### Step-by-Step Process

1. **Ocean Border Identification**:

   - Pacific: Top edge (row 0) and Left edge (col 0)
   - Atlantic: Bottom edge (row m-1) and Right edge (col n-1)

2. **DFS from Borders**: For each ocean, start DFS from all border cells

   - Mark cells reachable by following increasing/equal height paths
   - Use sets to track reachable cells for each ocean

3. **Find Intersection**: Cells reachable by both oceans can flow to both

### Example Walkthrough

For heights matrix:

```
1 2 2 3 5
3 2 3 4 4
2 4 5 3 1
6 7 1 4 5
5 1 1 2 4
```

**Pacific Border DFS:**

- From top: (0,0)→(0,1)→(0,2)→(0,3)→(0,4)
- From left: (0,0)→(1,0)→(2,0)→(3,0)→(4,0)
- Continue exploring connected higher cells...

**Atlantic Border DFS:**

- From bottom: (4,0)→(4,1)→(4,2)→(4,3)→(4,4)
- From right: (0,4)→(1,4)→(2,4)→(3,4)→(4,4)
- Continue exploring connected higher cells...

**Intersection Results:** `[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`

## Complexity Analysis

- **Time Complexity:** `O(m × n)` where m and n are matrix dimensions
  - Each cell is visited at most once per DFS (due to visited set)
  - We run DFS from border cells, but total visits across all DFS calls is O(m×n)
- **Space Complexity:** `O(m × n)` for the two sets storing reachable cells

## Key Insights

1. **Reverse Flow Logic**: Start from destination and work backwards
2. **Border Strategy**: Ocean borders are the starting points for reachability
3. **Set Intersection**: Efficient way to find cells reachable by both oceans
4. **Height Constraint**: Water flows from higher/equal to lower/equal heights

## Edge Cases

- **Single Cell**: Can always reach both oceans
- **All Same Height**: All cells can reach both oceans
- **Monotonic Heights**: Only certain patterns allow dual ocean access
- **Disconnected Regions**: Some areas may only reach one ocean

## Alternative Approaches

1. **BFS Approach**: Use queues instead of recursion for level-order exploration
2. **Union-Find**: Group connected components and check border connectivity
3. **Dynamic Programming**: Memoize reachability results for each cell

![Pacific Atlantic Water Flow Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754317977/Screenshot_2025-08-04_200245_dcc7dm.png)
