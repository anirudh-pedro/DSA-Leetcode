# 513. Find Bottom Left Tree Value

![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange)
![Tree](https://img.shields.io/badge/Topic-Tree-blue)
![BFS](https://img.shields.io/badge/Topic-BFS-orange)
![Binary Tree](https://img.shields.io/badge/Topic-Binary_Tree-green)

## Problem Description

Given the root of a binary tree, return the leftmost value in the last row of the tree.

## Examples

### Example 1:

```
Input: root = [2,1,3]
Output: 1
```

### Example 2:

```
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        res = None
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                res = node.val
        return res
```

## Algorithm Explanation

The solution uses **reverse-order BFS** to find the bottom-left value:

1. **Reverse Traversal Order**: Add right child first, then left child to the queue
2. **Level Processing**: Process all nodes level by level using BFS
3. **Last Node Tracking**: Keep updating `res` with each node's value
4. **Result Logic**: Due to reverse order, the last node processed will be the leftmost node of the bottom level

### Key Insight

- By adding right child before left child, we process nodes from right to left at each level
- The last node we process in the entire traversal will be the bottom-left node
- This clever ordering eliminates the need to explicitly track levels or positions

## Complexity Analysis

- **Time Complexity**: O(n) where n is the number of nodes
  - We visit each node exactly once
- **Space Complexity**: O(w) where w is the maximum width of the tree
  - The queue can contain at most all nodes at the widest level

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755154304/Screenshot_2025-08-14_122127_ydqkqv.png)
