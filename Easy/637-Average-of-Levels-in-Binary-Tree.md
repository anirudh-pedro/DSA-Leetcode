# 637. Average of Levels in Binary Tree

![LeetCode](https://img.shields.io/badge/LeetCode-Easy-green)
![Tree](https://img.shields.io/badge/Topic-Tree-blue)
![BFS](https://img.shields.io/badge/Topic-BFS-orange)

## Problem Description

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10^-5 of the actual answer will be accepted.

## Examples

### Example 1:

```
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
```

### Example 2:

```
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
```

## Constraints

- The number of nodes in the tree is in the range [1, 10^4]
- -2^31 <= Node.val <= 2^31 - 1

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = deque([root])
        while queue:
            k = len(queue)
            s = 0
            for _ in range(k):
                node = queue.popleft()
                s += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(s/k)
        return res
```

## Algorithm Explanation

The solution uses **level-order traversal (BFS)** to calculate averages level by level:

1. **Level-by-Level Processing**: Process all nodes at the current level before moving to the next
2. **Sum Calculation**: Keep track of the sum of all node values at the current level
3. **Count Tracking**: Use `k = len(queue)` to know exactly how many nodes are at the current level
4. **Average Computation**: Calculate average as `sum / count` and add to result array

### Key Insight

- We must process exactly `k` nodes (the number of nodes at current level) before calculating the average
- This ensures we don't mix nodes from different levels in our sum calculation
- The queue naturally separates levels as we add children after processing parents

## Complexity Analysis

- **Time Complexity**: O(n) where n is the number of nodes in the tree
  - We visit each node exactly once
- **Space Complexity**: O(w) where w is the maximum width of the tree
  - The queue can contain at most all nodes at the widest level

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755154456/Screenshot_2025-08-14_122405_k7ello.png)
