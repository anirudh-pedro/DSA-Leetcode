# 199. Binary Tree Right Side View

![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange)
![Tree](https://img.shields.io/badge/Topic-Tree-blue)
![BFS](https://img.shields.io/badge/Topic-BFS-orange)
![Binary Tree](https://img.shields.io/badge/Topic-Binary_Tree-green)

## Problem Description

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Examples

### Example 1:

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

### Example 2:

```
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
```

### Example 3:

```
Input: root = [1,null,3]
Output: [1,3]
```

### Example 4:

```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque(([root]))
        res.append(root.val)
        while queue:
            l = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue:
                res.append(queue[-1].val)
        return res
```

## Algorithm Explanation

The solution uses **level-order traversal (BFS)** with rightmost node capture:

1. **Initial Setup**: Add root value to result since it's always visible from the right
2. **Level Processing**: Process all nodes at the current level using BFS
3. **Queue Management**: Add children to queue for next level processing
4. **Rightmost Capture**: After processing a complete level, the last node added to queue (`queue[-1]`) is the rightmost visible node
5. **Visibility Logic**: Only nodes at the rightmost position of each level are visible from the right side

### Key Insight

- After processing all nodes at level i, the queue contains all nodes at level i+1
- The last node in the queue (`queue[-1]`) is always the rightmost node at that level
- This approach naturally captures the right side view without complex position tracking

## Complexity Analysis

- **Time Complexity**: O(n) where n is the number of nodes
  - We visit each node exactly once
- **Space Complexity**: O(w) where w is the maximum width of the tree
  - The queue can contain at most all nodes at the widest level

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755271909/Screenshot_2025-08-15_210044_om1chx.png)
