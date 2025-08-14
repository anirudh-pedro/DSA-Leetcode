# 116. Populating Next Right Pointers in Each Node

![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange)
![Tree](https://img.shields.io/badge/Topic-Tree-blue)
![BFS](https://img.shields.io/badge/Topic-BFS-orange)
![Binary Tree](https://img.shields.io/badge/Topic-Binary_Tree-green)

## Problem Description

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```cpp
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

## Examples

### Example 1:

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

### Example 2:

```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range [0, 2^12 - 1]
- -1000 <= Node.val <= 1000

**Follow-up**: You may only use constant extra space. The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

## Solution

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = deque([root])
        while queue:
            li = []
            for i in range(len(queue)):
                node = queue.popleft()
                li.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for i in range(len(li) - 1):
                li[i].next = li[i+1]
        return root
```

## Algorithm Explanation

The solution uses **level-order traversal (BFS)** with level-wise connection:

1. **Level Collection**: For each level, collect all nodes in a temporary list `li`
2. **BFS Traversal**: Process nodes level by level using a queue
3. **Next Pointer Connection**: After collecting all nodes at a level, connect each node to its next right node
4. **Connection Logic**: For nodes at positions 0 to n-2, connect `li[i].next = li[i+1]`

### Key Insight

- We collect all nodes at each level first, then connect them sequentially
- The last node at each level naturally gets `next = None` (default)
- This approach works for any binary tree structure, not just perfect trees

## Complexity Analysis

- **Time Complexity**: O(n) where n is the number of nodes
  - We visit each node exactly once
- **Space Complexity**: O(w) where w is the maximum width of the tree
  - We store at most one level of nodes in the list and queue

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755153995/Screenshot_2025-08-14_121451_uxjmfw.png)
