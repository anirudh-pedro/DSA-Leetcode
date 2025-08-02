# 332. Reconstruct Itinerary

## Problem Description

You are given a list of airline tickets where `tickets[i] = [fromi, toi]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from **"JFK"**, thus, the itinerary must begin with **"JFK"**. If there are multiple valid itineraries, you should return the itinerary that has the **smallest lexical order** when read as a single string.

For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.

You may assume all tickets form at least one valid itinerary. You must use all tickets **once and only once**.

## Examples

### Example 1:

```
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
```

### Example 2:

```
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
```

**Explanation:**
Another possible reconstruction is `["JFK","SFO","ATL","JFK","ATL","SFO"]` but it is larger in lexical order.

## Constraints

- `1 <= tickets.length <= 300`
- `tickets[i].length == 2`
- `fromi.length == 3`
- `toi.length == 3`
- `fromi` and `toi` consist of uppercase English letters
- `fromi != toi`

## Solution

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build adjacency list with destinations in reverse lexical order
        d = defaultdict(list)

        # Sort tickets in reverse order for lexically smallest result
        for departure, arrival in sorted(tickets, reverse=True):
            d[departure].append(arrival)

        stack = ["JFK"]  # Start from JFK
        res = []  # Result path (in reverse order initially)

        # Hierholzer's algorithm for Eulerian path
        while stack:
            # If current airport has outgoing flights
            while d[stack[-1]]:
                # Take the lexically smallest flight (due to reverse sorting + pop)
                next_airport = d[stack[-1]].pop()
                stack.append(next_airport)

            # No more outgoing flights, add to result
            res.append(stack.pop())

        # Reverse to get correct order
        return res[::-1]
```

## Algorithm Explanation

This solution uses **Hierholzer's Algorithm** to find an Eulerian path in a directed graph:

### Step 1: Build Graph with Lexical Ordering

- Create adjacency list from tickets
- Sort tickets in **reverse lexical order** before building the graph
- This ensures that when we `pop()` from the list, we get the lexically smallest destination

### Step 2: Hierholzer's Algorithm

- Start from "JFK" using a stack
- **DFS Traversal**: Follow edges until no more outgoing edges exist
- **Backtrack**: When stuck, add current node to result and backtrack
- Continue until all edges are used

### Step 3: Construct Final Path

- The algorithm builds the path in reverse order
- Reverse the result to get the correct itinerary

## Why Reverse Sorting Works

### Key Insight:

- We want lexically **smallest** destinations first
- Using `pop()` gives us the **last** element in the list
- Sorting in **reverse order** + `pop()` = getting smallest elements first

### Example:

```python
# From JFK, we can go to ["ATL", "SFO"]
# After reverse sorting: ["SFO", "ATL"]
# pop() gives "ATL" (lexically smaller)
```

## Step-by-Step Example (tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])

### Step 1: Build Adjacency List

```
After sorting tickets in reverse:
[["SFO","ATL"], ["JFK","SFO"], ["JFK","ATL"], ["ATL","SFO"], ["ATL","JFK"]]

Adjacency List:
JFK: ["SFO", "ATL"]  # Note: reverse order
ATL: ["SFO", "JFK"]  # Note: reverse order
SFO: ["ATL"]
```

### Step 2: Hierholzer's Algorithm Execution

| Step | Stack                                 | Current | Action      | d[current] | Result                                |
| ---- | ------------------------------------- | ------- | ----------- | ---------- | ------------------------------------- |
| 1    | ["JFK"]                               | JFK     | pop() "ATL" | ["SFO"]    | []                                    |
| 2    | ["JFK","ATL"]                         | ATL     | pop() "JFK" | ["SFO"]    | []                                    |
| 3    | ["JFK","ATL","JFK"]                   | JFK     | pop() "SFO" | []         | []                                    |
| 4    | ["JFK","ATL","JFK","SFO"]             | SFO     | pop() "ATL" | []         | []                                    |
| 5    | ["JFK","ATL","JFK","SFO","ATL"]       | ATL     | pop() "SFO" | []         | []                                    |
| 6    | ["JFK","ATL","JFK","SFO","ATL","SFO"] | SFO     | No edges    | []         | ["SFO"]                               |
| 7    | ["JFK","ATL","JFK","SFO","ATL"]       | ATL     | No edges    | []         | ["SFO","ATL"]                         |
| 8    | ["JFK","ATL","JFK","SFO"]             | SFO     | No edges    | []         | ["SFO","ATL","SFO"]                   |
| 9    | ["JFK","ATL","JFK"]                   | JFK     | No edges    | []         | ["SFO","ATL","SFO","JFK"]             |
| 10   | ["JFK","ATL"]                         | ATL     | No edges    | []         | ["SFO","ATL","SFO","JFK","ATL"]       |
| 11   | ["JFK"]                               | JFK     | No edges    | []         | ["SFO","ATL","SFO","JFK","ATL","JFK"] |

### Step 3: Reverse Result

```
res = ["SFO","ATL","SFO","JFK","ATL","JFK"]
return res[::-1] = ["JFK","ATL","JFK","SFO","ATL","SFO"]
```

## Graph Theory Background

### Eulerian Path Properties:

- **Eulerian Path**: Path that visits every edge exactly once
- **Conditions**: At most 2 nodes with odd degree (start and end nodes)
- **Hierholzer's Algorithm**: Efficient method to find Eulerian paths

### Why It Works for This Problem:

- Each ticket represents a directed edge
- We need to use each edge (ticket) exactly once
- "JFK" is guaranteed as the starting point
- The graph is guaranteed to have an Eulerian path

## Time and Space Complexity

- **Time Complexity**: O(E log E + E)
  - O(E log E) for sorting tickets
  - O(E) for Hierholzer's algorithm (each edge visited once)
- **Space Complexity**: O(E) for adjacency list and stack

## Key Insights

1. **Eulerian Path Problem**: Recognize this as finding a path using all edges once
2. **Lexical Ordering Trick**: Reverse sort + pop() gives smallest elements first
3. **Hierholzer's Algorithm**: Efficient method for Eulerian path construction
4. **Stack-based DFS**: Natural way to implement the algorithm
5. **Reverse Construction**: Algorithm builds path backwards, requiring final reversal

## Why This Approach Works

- **Correctness**: Hierholzer's algorithm guarantees finding Eulerian path if one exists
- **Lexical Ordering**: Reverse sorting ensures smallest valid path is chosen
- **Efficiency**: O(E log E) is optimal since we need to sort for lexical order
- **Simplicity**: Stack-based approach is elegant and easy to understand

## Alternative Approaches

1. **Backtracking DFS**: O(E!) worst case - too slow for larger inputs
2. **Recursive DFS**: Similar to Hierholzer's but with recursion instead of stack
3. **Modified Dijkstra**: Overkill and doesn't handle lexical ordering naturally

## Edge Cases Handled

1. **Single Ticket**: Works correctly with minimal path
2. **Multiple Paths from JFK**: Lexical ordering ensures smallest is chosen
3. **Cycles in Graph**: Hierholzer's handles cycles correctly
4. **Linear Path**: Works for simple chain of destinations

## Hierholzer's Algorithm Benefits

- **Guaranteed Solution**: Always finds Eulerian path if one exists
- **Linear Time**: Each edge processed exactly once (after sorting)
- **Memory Efficient**: Uses stack space proportional to longest path
- **Handles Cycles**: Naturally deals with complex graph structures

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754154473/Screenshot_2025-08-02_223731_nmdmzn.png)
