# 207. Course Schedule

## Problem Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]` indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

## Examples

### Example 1:

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
```

**Explanation:**
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

### Example 2:

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
```

**Explanation:**
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- All the pairs `prerequisites[i]` are unique

## Solution

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list: course -> list of prerequisites
        d = defaultdict(list)
        for i, j in prerequisites:
            d[i].append(j)

        # Keep track of nodes in current DFS path (cycle detection)
        visit = set()

        def back(cro):
            # If course is in current path, we found a cycle
            if cro in visit:
                return False

            # If course has no prerequisites, it can be completed
            if d[cro] == []:
                return True

            # Add current course to path
            visit.add(cro)

            # Check all prerequisites
            for v in d[cro]:
                if not back(v):
                    return False

            # Remove from path (backtrack)
            visit.remove(cro)
            # Mark as processed (no prerequisites needed)
            d[cro] = []
            return True

        # Check each course
        for i in range(numCourses):
            if not back(i):
                return False

        return True
```

## Algorithm Explanation

This solution uses **DFS with cycle detection** to determine if all courses can be completed:

### Step 1: Build Adjacency List

- Create a graph where each course points to its prerequisites
- `d[course] = [prerequisite1, prerequisite2, ...]`

### Step 2: DFS with Cycle Detection

- Use a `visit` set to track nodes in the current DFS path
- For each course, recursively check if all prerequisites can be completed
- If we encounter a course already in the current path, we found a cycle

### Step 3: Optimization - Memoization

- Once a course is verified as completable, clear its prerequisites (`d[cro] = []`)
- This prevents redundant checks and improves performance

### Step 4: Check All Courses

- Run DFS for every course to ensure all can be completed
- Return `False` if any course cannot be completed due to cycles

## Detailed Algorithm Flow

### Cycle Detection Logic:

1. **Enter course**: Add to `visit` set (current path)
2. **Check prerequisites**: Recursively verify each prerequisite
3. **Cycle found**: If prerequisite is already in current path → cycle detected
4. **Backtrack**: Remove from `visit` set when done
5. **Memoize**: Clear prerequisites list to avoid rechecking

### Example Walkthrough (numCourses = 2, prerequisites = [[1,0],[0,1]]):

| Step | Course | Visit Set | Prerequisites | Result                          |
| ---- | ------ | --------- | ------------- | ------------------------------- |
| 1    | 0      | {0}       | [1]           | Check course 1                  |
| 2    | 1      | {0,1}     | [0]           | Check course 0                  |
| 3    | 0      | {0,1}     | [1]           | 0 already in visit → **Cycle!** |

Result: `False` (impossible to complete)

## Time and Space Complexity

- **Time Complexity**: O(V + E) where V = numCourses, E = prerequisites.length
  - Each course and prerequisite relationship is visited once
- **Space Complexity**: O(V + E) for the adjacency list and recursion stack

## Key Insights

1. **Graph Representation**: Model as a directed graph where edges represent dependencies
2. **Cycle Detection**: Use DFS with path tracking to detect cycles
3. **Topological Sort**: This problem is essentially checking if a topological sort exists
4. **Memoization**: Clear processed prerequisites to avoid redundant work
5. **Backtracking**: Properly manage the visit set to track only the current path

## Alternative Approaches

1. **Kahn's Algorithm**: Use indegree counting for topological sort
2. **Union-Find**: Can be adapted but DFS is more intuitive for this problem

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1751735508/Screenshot_2025-07-05_223927_xae9eb.png)
