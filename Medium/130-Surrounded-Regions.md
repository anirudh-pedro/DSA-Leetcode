# 130. Surrounded Regions

**Difficulty:** Medium  
**Topics:** Array, Depth-First Search, Breadth-First Search, Union Find, Matrix  
**Companies:** Amazon, Microsoft, Google

## Problem Description

You are given an `m x n` matrix `board` containing letters `'X'` and `'O'`. **Capture regions that are surrounded**:

- **Connect**: A cell is connected to adjacent cells horizontally or vertically
- **Region**: To form a region, connect every `'O'` cell
- **Surround**: The region is surrounded with `'X'` cells if you can connect the region with `'X'` cells and none of the region cells are on the edge of the board

To capture a surrounded region, **replace all `'O'`s with `'X'`s** in-place within the original board.

## Examples

### Example 1:

```
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
```

### Example 2:

```
Input: board = [["X"]]
Output: [["X"]]
```

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`

## Solution

```python
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def mark_unsurrounded(r, c):
            """
            DFS to mark all 'O' cells connected to border as 'T' (temporary).
            These cells cannot be surrounded.
            """
            # Base case: out of bounds or not an 'O' cell
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return

            # Mark as temporary to indicate it's connected to border
            board[r][c] = "T"

            # Explore all 4 directions
            mark_unsurrounded(r + 1, c)  # Down
            mark_unsurrounded(r - 1, c)  # Up
            mark_unsurrounded(r, c + 1)  # Right
            mark_unsurrounded(r, c - 1)  # Left

        # Step 1: Mark all 'O's connected to borders as 'T'
        # Check all border cells
        for i in range(rows):
            for j in range(cols):
                # If it's a border cell and contains 'O'
                if (i in [0, rows-1] or j in [0, cols-1]) and board[i][j] == "O":
                    mark_unsurrounded(i, j)

        # Step 2: Convert remaining 'O's to 'X' (these are surrounded)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # Step 3: Convert 'T's back to 'O' (these are unsurrounded)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"
```

## Algorithm Explanation

This solution uses **reverse thinking with DFS** - instead of finding surrounded regions, we find **unsurrounded regions** first:

### Key Insight

- **Surrounded regions** cannot reach the border
- **Unsurrounded regions** are connected to at least one border cell
- Mark all unsurrounded regions first, then convert the remaining 'O's

### Step-by-Step Process

1. **Border Traversal**: Check all cells on the border of the matrix
2. **DFS Marking**: For each border 'O', use DFS to mark all connected 'O's as temporary ('T')
3. **Surrounded Conversion**: Convert all remaining 'O's to 'X' (these are truly surrounded)
4. **Restoration**: Convert all 'T's back to 'O' (these are unsurrounded)

### Example Walkthrough

For the input matrix:

```
X X X X
X O O X
X X O X
X O X X
```

**Step 1 - Mark border-connected 'O's:**

```
X X X X
X O O X
X X O X
X T X X  ← Border 'O' marked as 'T'
```

**Step 2 - Convert remaining 'O's to 'X':**

```
X X X X
X X X X  ← These 'O's were surrounded
X X X X
X T X X
```

**Step 3 - Convert 'T's back to 'O':**

```
X X X X
X X X X
X X X X
X O X X  ← Final result
```

## Complexity Analysis

- **Time Complexity:** `O(m × n)` where m and n are matrix dimensions
  - In worst case, we visit every cell once during DFS
- **Space Complexity:** `O(m × n)` in worst case
  - Due to recursion stack depth (when entire matrix is connected 'O's)

## Key Insights

1. **Reverse Logic**: Instead of finding surrounded, find unsurrounded regions
2. **Border Strategy**: Only border-connected regions can be unsurrounded
3. **Three-State Marking**: Use temporary marker 'T' to distinguish processing states
4. **In-place Modification**: No additional space needed for result storage

## Edge Cases

- **All 'X'**: No changes needed
- **All 'O'**: All remain 'O' (connected to border)
- **Single Cell**: If 'O', it remains 'O' (it's on border)
- **Border 'O's**: Always remain 'O'

## Alternative Approaches

1. **BFS Approach**: Use queue instead of recursion for level-order traversal
2. **Union-Find**: Group connected components and check border connectivity
3. **Iterative DFS**: Use explicit stack to avoid recursion depth issues

![Surrounded Regions Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754317872/Screenshot_2025-08-04_200050_n3bmpk.png)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4a106260-9e2e-4e2e-a067-0cf423b8b199" />

