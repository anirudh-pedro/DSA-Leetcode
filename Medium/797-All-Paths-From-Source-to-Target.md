# 797. All Paths From Source to Target

![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange)
![Graph](https://img.shields.io/badge/Topic-Graph-blue)
![DFS](https://img.shields.io/badge/Topic-DFS-red)
![Backtracking](https://img.shields.io/badge/Topic-Backtracking-purple)

## Problem Description

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to `graph[i][j]`).

## Examples

### Example 1:

```
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
```

### Example 2:

```
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```

## Constraints

- n == graph.length
- 2 <= n <= 15
- 0 <= graph[i][j] < n
- graph[i][j] != i (i.e., there will be no self-loops)
- All the elements of graph[i] are unique
- The input graph is guaranteed to be a DAG

## Solution

```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        if not graph:
            return []
        for i,edge in enumerate(graph):
            d[i] = edge
        res = []
        def back(li,node):
            if node == len(graph) - 1:
                res.append(li.copy())
                return
            for v in d[node]:
                li.append(v)
                back(li,v)
                li.pop()
        back([0],0)
        return res
```

## Algorithm Explanation

The solution uses **backtracking DFS** to explore all possible paths:

1. **Graph Representation**: Convert input to adjacency list using defaultdict
2. **Path Tracking**: Use list `li` to track current path from source
3. **Base Case**: When we reach the target node (`len(graph) - 1`), add path copy to results
4. **Backtracking**: For each neighbor, add to path, recurse, then remove (backtrack)
5. **Path Exploration**: Systematically explore all possible paths using DFS

### Key Insight

- We use backtracking to explore all paths without creating separate path copies for each branch
- The `li.copy()` ensures we store the current path state in results
- Backtracking (`li.pop()`) allows us to reuse the same path list for different branches

## Complexity Analysis

- **Time Complexity**: O(2^n × n) where n is the number of nodes
  - In worst case, there could be 2^n paths, each of length n
- **Space Complexity**: O(n) for the recursion stack and current path storage
  - Not counting the output space

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755155357/Screenshot_2025-08-14_123904_z3y5kl.png)
