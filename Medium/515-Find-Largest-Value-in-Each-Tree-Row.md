# 515. Find Largest Value in Each Tree Row

![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange)
![Tree](https://img.shields.io/badge/Topic-Tree-blue)
![BFS](https://img.shields.io/badge/Topic-BFS-orange)
![Binary Tree](https://img.shields.io/badge/Topic-Binary_Tree-green)

## Problem Description

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

## Examples

### Example 1:

```
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
```

### Example 2:

```
Input: root = [1,2,3]
Output: [1,3]
```

## Constraints

- The number of nodes in the tree will be in the range [0, 10^4]
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            ma = float('-inf')
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.val > ma:
                    ma = node.val
            res.append(ma)
        return res
```

## Algorithm Explanation

The solution uses **level-order traversal (BFS)** to find the maximum value at each level:

1. **Level Processing**: Process all nodes at the current level before moving to the next
2. **Maximum Tracking**: Initialize `ma` to negative infinity for each level
3. **Value Comparison**: Compare each node's value with the current maximum
4. **Level Maximum**: After processing all nodes at a level, add the maximum to result

### Key Insight

- We process exactly `len(queue)` nodes at each level to avoid mixing levels
- Using `float('-inf')` handles the case where all values at a level might be negative
- The BFS approach naturally processes the tree level by level

## Complexity Analysis

- **Time Complexity**: O(n) where n is the number of nodes
  - We visit each node exactly once
- **Space Complexity**: O(w) where w is the maximum width of the tree
  - The queue can contain at most all nodes at the widest level

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755154701/Screenshot_2025-08-14_122808_nfwvk3.png)
