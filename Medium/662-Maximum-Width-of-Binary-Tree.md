# 662. Maximum Width of Binary Tree

![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange)
![Tree](https://img.shields.io/badge/Topic-Tree-blue)
![BFS](https://img.shields.io/badge/Topic-BFS-orange)
![Binary Tree](https://img.shields.io/badge/Topic-Binary_Tree-green)

## Problem Description

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will be in the range of a 32-bit signed integer.

## Examples

### Example 1:

```
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
```

### Example 2:

```
Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
```

### Example 3:

```
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
```

## Constraints

- The number of nodes in the tree is in the range [1, 3000]
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root,0)])
        mawi = 0
        while queue:
            start = queue[0][1]
            for i in range(len(queue)):
                node, ind = queue.popleft()
                if node.left:
                    queue.append((node.left,2 * ind))
                if node.right:
                    queue.append((node.right,2*ind + 1))
            mawi = max(mawi,ind - start + 1)
        return mawi
```

## Algorithm Explanation

The solution uses **level-order traversal (BFS)** with positional indexing:

1. **Node Indexing**: Each node is paired with its position index in a complete binary tree
2. **Index Assignment**:
   - Left child gets index `2 * parent_index`
   - Right child gets index `2 * parent_index + 1`
3. **Level Width Calculation**: For each level, width = `rightmost_index - leftmost_index + 1`
4. **Width Tracking**: Track the maximum width encountered across all levels
5. **Start Position**: Use `queue[0][1]` as the leftmost position at current level

### Key Insight

- We assign each node a position as if the tree were complete (like heap indexing)
- The width of a level is the difference between the rightmost and leftmost positions plus 1
- This approach naturally handles null nodes in the width calculation without explicitly storing them

## Complexity Analysis

- **Time Complexity**: O(n) where n is the number of nodes
  - We visit each node exactly once
- **Space Complexity**: O(w) where w is the maximum width of the tree
  - The queue can contain at most all nodes at the widest level

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755272013/Screenshot_2025-08-15_210321_kjpgpf.png)
