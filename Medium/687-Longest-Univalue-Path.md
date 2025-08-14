# 687. Longest Univalue Path

![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange)
![Tree](https://img.shields.io/badge/Topic-Tree-blue)
![DFS](https://img.shields.io/badge/Topic-DFS-red)
![Binary Tree](https://img.shields.io/badge/Topic-Binary_Tree-green)

## Problem Description

Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

## Examples

### Example 1:

```
Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).
```

### Example 2:

```
Input: root = [1,4,5,4,4,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 4).
```

## Constraints

- The number of nodes in the tree is in the range [0, 10^4]
- -1000 <= Node.val <= 1000
- The depth of the tree will not exceed 1000

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0
        def back(root):
            if not root:
                return (float('-inf'),0)
            if not root.left and not root.right:
                return (root.val,0)
            lv,lw = back(root.left)
            rv,rw = back(root.right)
            if lv == rv == root.val:
                self.res = max(self.res,2 + lw + rw)
                return (root.val,1 + max(lw,rw))
            elif lv == root.val:
                self.res = max(self.res,1 + lw)
                return (root.val,1 + lw)
            elif rv == root.val:
                self.res = max(self.res,1 + rw)
                return (root.val,1 + rw)
            else:
                return (root.val,0)
        back(root)
        return self.res
```

## Algorithm Explanation

The solution uses **post-order DFS** with path extension tracking:

1. **Return Format**: Each recursive call returns `(value, max_path_length)` from current node
2. **Base Cases**:
   - Null node returns `(float('-inf'), 0)`
   - Leaf node returns `(node.val, 0)`
3. **Path Extension Logic**:
   - If both children have same value as root: path can go through root connecting both sides
   - If only one child matches: extend path from that side
   - If neither matches: start new path from root
4. **Global Maximum**: Update `self.res` with the longest path found at each node

### Key Insight

- We track both the node's value and the longest univalue path extending from it
- At each node, we can either extend existing paths or start new ones
- The global result considers all possible univalue paths in the tree

## Complexity Analysis

- **Time Complexity**: O(n) where n is the number of nodes
  - We visit each node exactly once
- **Space Complexity**: O(h) where h is the height of the tree
  - Recursion stack space for DFS traversal

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755155231/Screenshot_2025-08-14_123658_shdko3.png)
