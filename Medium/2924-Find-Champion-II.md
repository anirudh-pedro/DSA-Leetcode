# 2924. Find Champion II

## Problem Description

There are `n` teams numbered from `0` to `n - 1` in a tournament; each team is also a node in a **DAG** (Directed Acyclic Graph).

You are given the integer `n` and a 0-indexed 2D integer array `edges` of length `m` representing the DAG, where `edges[i] = [ui, vi]` indicates that there is a directed edge from team `ui` to team `vi` in the graph.

A directed edge from `a` to `b` in the graph means that **team `a` is stronger than team `b`** and **team `b` is weaker than team `a`**.

Team `a` will be the **champion** of the tournament if there is **no team `b` that is stronger than team `a`**.

Return the team that will be the champion of the tournament if there is a **unique champion**, otherwise, return **-1**.

### Notes:

- A **cycle** is a series of nodes a₁, a₂, ..., aₙ, aₙ₊₁ such that node a₁ is the same node as aₙ₊₁
- A **DAG** is a directed graph that does not have any cycle

## Examples

### Example 1:

```
Input: n = 3, edges = [[0,1],[1,2]]
Output: 0
```

**Explanation:**
Team 1 is weaker than team 0. Team 2 is weaker than team 1. So the champion is team 0.

### Example 2:

```
Input: n = 4, edges = [[0,2],[1,3],[1,2]]
Output: -1
```

**Explanation:**
Team 2 is weaker than team 0 and team 1. Team 3 is weaker than team 1. But team 1 and team 0 are not weaker than any other teams. So the answer is -1.

## Constraints

- `1 <= n <= 100`
- `m == edges.length`
- `0 <= m <= n * (n - 1) / 2`
- `edges[i].length == 2`
- `0 <= edge[i][j] <= n - 1`
- `edges[i][0] != edges[i][1]`
- The input is generated such that if team `a` is stronger than team `b`, team `b` is not stronger than team `a`
- The input is generated such that if team `a` is stronger than team `b` and team `b` is stronger than team `c`, then team `a` is stronger than team `c`

## Solution

```python
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Count indegree for each team (how many teams are stronger)
        d = defaultdict(int)
        for u, v in edges:
            d[v] += 1  # Team v has one more stronger team (u)

        chap = -1  # Champion candidate
        cou = 0    # Count of teams with indegree 0

        # Find teams with indegree 0 (no stronger teams)
        for i in range(n):
            if d[i] == 0:  # Team i has no stronger teams
                cou += 1
                chap = i

        # Return champion only if there's exactly one team with indegree 0
        return chap if cou == 1 else -1
```

## Algorithm Explanation

This solution uses **indegree counting** to find the champion:

### Step 1: Build Indegree Count

- For each edge `[u, v]`, increment the indegree of team `v`
- Indegree represents the number of teams stronger than the current team
- Use `defaultdict(int)` to handle teams with 0 indegree automatically

### Step 2: Find Teams with Zero Indegree

- A team with indegree 0 means no other team is stronger than it
- Such a team is a potential champion
- Count how many teams have indegree 0

### Step 3: Determine Champion

- If exactly **one team** has indegree 0 → That team is the unique champion
- If **zero teams** have indegree 0 → Impossible (contradiction with DAG property)
- If **multiple teams** have indegree 0 → No unique champion, return -1

## Step-by-Step Example

### Example 1: n = 3, edges = [[0,1],[1,2]]

| Team | Incoming Edges | Indegree | Champion? |
| ---- | -------------- | -------- | --------- |
| 0    | None           | 0        | ✓         |
| 1    | From 0         | 1        | ✗         |
| 2    | From 1         | 1        | ✗         |

**Result**: Team 0 (unique champion)

### Example 2: n = 4, edges = [[0,2],[1,3],[1,2]]

| Team | Incoming Edges | Indegree | Champion? |
| ---- | -------------- | -------- | --------- |
| 0    | None           | 0        | ✓         |
| 1    | None           | 0        | ✓         |
| 2    | From 0,1       | 2        | ✗         |
| 3    | From 1         | 1        | ✗         |

**Result**: -1 (multiple potential champions: 0 and 1)

## Graph Theory Perspective

### Champion Definition:

- A team is a champion if it's a **source node** in the DAG
- Source node: A node with **indegree = 0** (no incoming edges)

### Why Indegree Works:

- **Indegree = 0**: No team is stronger → Potential champion
- **Indegree > 0**: At least one team is stronger → Cannot be champion
- **Unique champion**: Exactly one source node exists
- **No unique champion**: Multiple source nodes exist

## Time and Space Complexity

- **Time Complexity**: O(m + n)
  - O(m) to process all edges and build indegree count
  - O(n) to check indegree of all teams
- **Space Complexity**: O(n) for the indegree dictionary

## Key Insights

1. **Graph Modeling**: Tournament strength relationships form a DAG
2. **Source Node Identification**: Champion is a source node (indegree 0)
3. **Uniqueness Check**: Exactly one source node means unique champion
4. **Efficient Counting**: Single pass through edges to build indegree
5. **DAG Property**: Guarantees no cycles, making indegree analysis valid

## Why This Approach Works

- **Mathematical Foundation**: In a DAG representing tournament, the champion must be a source node
- **Efficiency**: O(m + n) is optimal since we need to examine all edges and teams
- **Correctness**: Indegree counting directly captures the "stronger than" relationships
- **Edge Cases**: Handles multiple champions and impossible scenarios correctly

## Alternative Approaches

1. **Topological Sort**: More complex but would also work
2. **DFS from each node**: Less efficient O(n × (n + m))
3. **Matrix representation**: Higher space complexity O(n²)

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754072193/Screenshot_2025-08-01_234452_uizswn.png)
