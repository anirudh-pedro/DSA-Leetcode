# 3243. Shortest Distance After Road Addition Queries I

## Problem Description

You are given an integer `n` and a 2D integer array `queries`.

There are `n` cities numbered from `0` to `n - 1`. Initially, there is a **unidirectional road** from city `i` to city `i + 1` for all `0 <= i < n - 1`.

`queries[i] = [ui, vi]` represents the addition of a new **unidirectional road** from city `ui` to city `vi`. After each query, you need to find the **length of the shortest path** from city `0` to city `n - 1`.

Return an array `answer` where for each `i` in the range `[0, queries.length - 1]`, `answer[i]` is the length of the shortest path from city `0` to city `n - 1` after processing the first `i + 1` queries.

## Examples

### Example 1:

```
Input: n = 5, queries = [[2,4],[0,2],[0,4]]
Output: [3,2,1]
```

**Explanation:**

- After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3
- After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2
- After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1

### Example 2:

```
Input: n = 4, queries = [[0,3],[0,2]]
Output: [1,1]
```

**Explanation:**

- After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1
- After the addition of the road from 0 to 2, the length of the shortest path remains 1

## Constraints

- `3 <= n <= 500`
- `1 <= queries.length <= 500`
- `queries[i].length == 2`
- `0 <= queries[i][0] < queries[i][1] < n`
- `1 < queries[i][1] - queries[i][0]`
- There are no repeated roads among the queries

## Solution

```python
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        # Initialize adjacency list with initial roads (i -> i+1)
        adli = [[] for i in range(n)]
        for i in range(n - 1):
            adli[i].append(i + 1)

        def bfs(n, adli):
            """BFS to find shortest path from city 0 to city n-1"""
            visit = [False] * n
            queue = deque([0])
            visit[0] = True  # Mark starting city as visited
            step = 0

            while queue:
                # Process all nodes at current level
                for i in range(len(queue)):
                    node = queue.popleft()

                    # If we reached the destination
                    if node == n - 1:
                        return step

                    # Explore all neighbors
                    for neighbor in adli[node]:
                        if not visit[neighbor]:
                            queue.append(neighbor)
                            visit[neighbor] = True

                step += 1  # Move to next level

            return -1  # Path not found (shouldn't happen in this problem)

        # Process each query
        for u, v in queries:
            adli[u].append(v)  # Add new road from u to v
            ans.append(bfs(n, adli))  # Find shortest path after adding road

        return ans
```

## Algorithm Explanation

This solution uses **BFS (Breadth-First Search)** after each query to find the shortest path:

### Step 1: Initialize Graph

- Create adjacency list representation of the city network
- Initially, each city `i` connects to city `i + 1` (linear path)

### Step 2: Process Each Query

- Add the new road `[u, v]` to the adjacency list
- Run BFS to find the new shortest path from city 0 to city n-1
- Store the result in the answer array

### Step 3: BFS Implementation

- **Level-order traversal**: Process all cities at distance `d` before moving to distance `d+1`
- **Early termination**: Return immediately when destination is reached
- **Visited tracking**: Avoid revisiting cities to prevent infinite loops

## Step-by-Step Example (n = 5, queries = [[2,4],[0,2],[0,4]])

### Initial State:

```
Cities: 0 -> 1 -> 2 -> 3 -> 4
Path 0 to 4: 0 -> 1 -> 2 -> 3 -> 4 (length = 4)
```

### After Query 1: [2,4]

```
Cities: 0 -> 1 -> 2 -> 3 -> 4
              ↓         ↗
              4 ←--------
Path 0 to 4: 0 -> 1 -> 2 -> 4 (length = 3)
```

### After Query 2: [0,2]

```
Cities: 0 -> 1 -> 2 -> 3 -> 4
        ↓         ↓         ↗
        2 --------4 ←--------
Path 0 to 4: 0 -> 2 -> 4 (length = 2)
```

### After Query 3: [0,4]

```
Cities: 0 -> 1 -> 2 -> 3 -> 4
        ↓    ↓    ↓         ↗
        2 ---4 ---4 ←--------
        ↓         ↗
        4 ←--------
Path 0 to 4: 0 -> 4 (length = 1)
```

## BFS Execution Details

| Query | New Road | BFS Levels    | Shortest Path | Distance |
| ----- | -------- | ------------- | ------------- | -------- |
| [2,4] | 2→4      | 0→{1,2}→{3,4} | 0→1→2→4       | 3        |
| [0,2] | 0→2      | 0→{1,2}→{3,4} | 0→2→4         | 2        |
| [0,4] | 0→4      | 0→{1,2,4}     | 0→4           | 1        |

## Time and Space Complexity

- **Time Complexity**: O(Q × (V + E))
  - Q = number of queries (up to 500)
  - V = number of cities (up to 500)
  - E = number of roads (up to Q + n)
  - Each BFS takes O(V + E) time
- **Space Complexity**: O(V + E) for adjacency list and BFS data structures

## Key Insights

1. **Dynamic Graph Updates**: Graph changes after each query, requiring fresh shortest path calculation
2. **BFS for Unweighted Shortest Path**: BFS guarantees shortest path in unweighted graphs
3. **Level-by-Level Processing**: BFS processes cities by distance, ensuring optimality
4. **Early Termination**: Stop as soon as destination is reached
5. **Graph Representation**: Adjacency list efficiently handles dynamic road additions

## Why This Approach Works

- **Correctness**: BFS finds shortest path in unweighted graphs
- **Efficiency**: Early termination saves unnecessary exploration
- **Simplicity**: Straightforward implementation without complex data structures
- **Robustness**: Handles all edge cases including direct connections

## Alternative Approaches

1. **Dijkstra's Algorithm**: Overkill for unweighted graphs
2. **Floyd-Warshall**: O(n³) per query, too slow
3. **Bidirectional BFS**: Could optimize for larger graphs
4. **Incremental Shortest Path**: More complex but potentially faster for many queries

## Optimization Opportunities

For larger constraints, consider:

- **Bidirectional BFS**: Search from both ends
- **A\* Algorithm**: With appropriate heuristic
- **Incremental algorithms**: Update shortest paths without full recalculation

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754072394/Screenshot_2025-08-01_234925_xkhu9f.png)
