# 429. N-ary Tree Level Order Traversal

![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange)
![Tree](https://img.shields.io/badge/Topic-Tree-blue)
![BFS](https://img.shields.io/badge/Topic-BFS-orange)
![N-ary Tree](https://img.shields.io/badge/Topic-N--ary_Tree-green)

## Problem Description

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.

## Examples

### Example 1:

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
```

### Example 2:

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
```

## Constraints

- The height of the n-ary tree is less than or equal to 1000
- The total number of nodes is between [0, 10^4]

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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = deque([root])
        res = []
        if not root:
            return res
        while queue:
            li = []
            for i in range(len(queue)):
                node = queue.popleft()
                for j in node.children:
                    if j:
                        queue.append(j)
                li.append(node.val)
            res.append(li)
        return res
```

## Algorithm Explanation

The solution uses **level-order traversal (BFS)** to collect nodes level by level:

1. **Base Case**: Handle empty tree by returning empty result
2. **Level Processing**: Use `len(queue)` to determine how many nodes are at the current level
3. **Children Addition**: For each node, add all its non-null children to the queue
4. **Level Collection**: Collect all node values at the current level in `li`
5. **Result Building**: Add each complete level to the result array

### Key Insight

- We process exactly `len(queue)` nodes at each level to avoid mixing levels
- N-ary trees can have any number of children, so we iterate through all children
- The queue naturally maintains the BFS order for level-by-level processing

## Complexity Analysis

- **Time Complexity**: O(n) where n is the number of nodes
  - We visit each node exactly once
- **Space Complexity**: O(w) where w is the maximum width of the tree
  - The queue can contain at most all nodes at the widest level

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755154565/Screenshot_2025-08-14_122553_wnnrfw.png)
