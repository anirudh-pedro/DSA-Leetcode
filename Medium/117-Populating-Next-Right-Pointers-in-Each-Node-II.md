# 117. Populating Next Right Pointers in Each Node II

![LeetCode](https://img.shields.io/badge/LeetCode-Medium-orange)
![Tree](https://img.shields.io/badge/Topic-Tree-blue)
![BFS](https://img.shields.io/badge/Topic-BFS-orange)
![Binary Tree](https://img.shields.io/badge/Topic-Binary_Tree-green)

## Problem Description

Given a binary tree:

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
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

### Example 2:

```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range [0, 6000]
- -100 <= Node.val <= 100

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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque([root])
        while queue:
            k = len(queue)
            pre = None
            for i in range(k):
                node = queue.popleft()
                if pre:
                    pre.next = node
                pre = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
```

## Algorithm Explanation

The solution uses **level-order traversal (BFS)** with sequential connection:

1. **Level Processing**: Process exactly `k` nodes (nodes at current level) in each iteration
2. **Sequential Connection**: Use a `pre` pointer to connect the previous node to the current node
3. **Connection Logic**: As we process each node, connect the previous node's next pointer to current node
4. **Pointer Update**: Update `pre` to current node for next iteration

### Key Insight

- Instead of collecting all nodes first, we connect them as we process them
- The `pre` pointer keeps track of the previous node at the current level
- This approach is more memory-efficient as we don't need extra storage for level nodes

## Complexity Analysis

- **Time Complexity**: O(n) where n is the number of nodes
  - We visit each node exactly once
- **Space Complexity**: O(w) where w is the maximum width of the tree
  - Only the queue space is used, no additional level storage

## Visual Reference

![Solution Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1755154156/Screenshot_2025-08-14_121900_q4mwqw.png)
