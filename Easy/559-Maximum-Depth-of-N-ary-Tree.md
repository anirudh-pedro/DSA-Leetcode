# 559. Maximum Depth of N-ary Tree

![LeetCode](https://img.shields.io/badge/LeetCode-Easy-green)
![Tree](https://img.shields.io/badge/Topic-Tree-blue)
![BFS](https://img.shields.io/badge/Topic-BFS-orange)

## Problem Description

Given an n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.

## Examples

### Example 1:

```
Input: root = [1,null,3,2,4,null,5,6]
Output: 3
```

### Example 2:

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5
```

## Constraints

- The total number of nodes is in the range [0, 10^4]
- The depth of the n-ary tree is less than or equal to 1000

## Solution

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        dep = 0
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                for j in node.children:
                    if j:
                        queue.append(j)
            dep += 1
        return dep
```

## Algorithm Explanation

The solution uses **level-order traversal (BFS)** to find the maximum depth:

1. **Base Case**: If the root is None, return 0
2. **Level-by-Level Processing**: Use a queue to process nodes level by level
3. **Depth Counting**: For each complete level processed, increment the depth counter
4. **Children Addition**: For each node, add all its non-null children to the queue for the next level

### Key Insight

- We process nodes level by level, counting each complete level
- The depth increments after processing all nodes at the current level
- This ensures we count the number of levels from root to the deepest leaf

## Complexity Analysis

- **Time Complexity**: O(n) where n is the number of nodes in the tree
  - We visit each node exactly once
- **Space Complexity**: O(w) where w is the maximum width of the tree
  - The queue can contain at most all nodes at the widest level

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755154858/Screenshot_2025-08-14_123043_xsc1zk.png)
