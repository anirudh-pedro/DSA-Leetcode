# 623. Add One Row to Tree

![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange)
![Tree](https://img.shields.io/badge/Topic-Tree-blue)
![BFS](https://img.shields.io/badge/Topic-BFS-orange)
![Binary Tree](https://img.shields.io/badge/Topic-Binary_Tree-green)

## Problem Description

Given the root of a binary tree and two integers `val` and `depth`, add a row of nodes with value `val` at the given depth `depth`.

Note that the root node is at depth 1.

The adding rule is:

- Given the integer `depth`, for each not null tree node `cur` at the depth `depth - 1`, create two tree nodes with value `val` as `cur`'s left subtree root and right subtree root.
- `cur`'s original left subtree should be the left subtree of the new left subtree root.
- `cur`'s original right subtree should be the right subtree of the new right subtree root.
- If `depth == 1` that means there is no depth `depth - 1` at all, then create a tree node with value `val` as the new root of the whole original tree, and the original tree is the new root's left subtree.

## Examples

### Example 1:

```
Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]
```

### Example 2:

```
Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]
```

## Constraints

- The number of nodes in the tree is in the range [1, 10^4]
- The depth of the tree is in the range [1, 10^4]
- -100 <= Node.val <= 100
- -10^5 <= val <= 10^5
- 1 <= depth <= the depth of tree + 1

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val,root,None)

        queue = deque([root])
        le = 1
        while queue:
            if depth - 1 == le:
                break
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            le += 1
        for cur in queue:
            if cur.left:
                temp = cur.left
                cur.left = TreeNode(val,temp,None)
            else:
                cur.left = TreeNode(val,None,None)
            if cur.right:
                temp = cur.right
                cur.right = TreeNode(val,None,temp)
            else:
                cur.right = TreeNode(val,None,None)
        return root
```

## Algorithm Explanation

The solution uses **level-order traversal (BFS)** to reach the target depth:

1. **Special Case**: If depth is 1, create a new root with the original tree as left child
2. **Navigate to Target Level**: Use BFS to reach level `depth - 1` (parents of target depth)
3. **Level Tracking**: Use `le` counter to track current level during traversal
4. **Row Insertion**: For each parent node at `depth - 1`:
   - Create new left child with value `val`, original left child becomes its left child
   - Create new right child with value `val`, original right child becomes its right child

### Key Insight

- We need to modify nodes at `depth - 1` to insert the new row at `depth`
- Each parent gets two new children with value `val`, preserving the original subtrees
- The BFS approach efficiently navigates to the exact level we need to modify

## Complexity Analysis

- **Time Complexity**: O(n) where n is the number of nodes up to level `depth - 1`
  - In worst case, we might traverse the entire tree
- **Space Complexity**: O(w) where w is the maximum width of the tree
  - The queue can contain at most all nodes at the widest level

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755154975/Screenshot_2025-08-14_123245_ksbneu.png)
