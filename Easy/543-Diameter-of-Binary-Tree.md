# 543. Diameter of Binary Tree

**Difficulty:** Easy  
**Topics:** Tree, Depth-First Search, Binary Tree  
**Companies:** Amazon, Microsoft, Google

## Problem Description

Given the root of a binary tree, return the **length of the diameter** of the tree.

The diameter of a binary tree is the **length of the longest path between any two nodes** in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

## Examples

### Example 1:

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

### Example 2:

```
Input: root = [1,2]
Output: 1
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`
- `-100 <= Node.val <= 100`

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Variable to track the maximum diameter found
        max_diameter = 0

        def get_height(node):
            """
            Calculate height of subtree and update maximum diameter.
            Returns the height of the current subtree.
            """
            if not node:
                return 0

            # Get height of left and right subtrees
            left_height = get_height(node.left)
            right_height = get_height(node.right)

            # Update maximum diameter (path through current node)
            nonlocal max_diameter
            current_diameter = left_height + right_height
            max_diameter = max(max_diameter, current_diameter)

            # Return height of current subtree
            return 1 + max(left_height, right_height)

        get_height(root)
        return max_diameter
```

## Algorithm Explanation

This solution uses a **post-order DFS traversal** with the following approach:

### Key Insight

- The diameter of a tree is the longest path between any two nodes
- For any node, the longest path through it equals: `left_subtree_height + right_subtree_height`
- We need to check this for every node and return the maximum

### Step-by-Step Process

1. **Recursive Height Calculation**: For each node, calculate the height of its left and right subtrees
2. **Diameter Update**: At each node, calculate the diameter passing through it (sum of left and right heights)
3. **Global Maximum**: Keep track of the maximum diameter seen so far
4. **Height Return**: Return the height of the current subtree for parent calculations

### Example Walkthrough

For tree `[1,2,3,4,5]`:

```
      1
     / \
    2   3
   / \
  4   5
```

| Node | Left Height | Right Height | Diameter Through Node | Max Diameter |
| ---- | ----------- | ------------ | --------------------- | ------------ |
| 4    | 0           | 0            | 0                     | 0            |
| 5    | 0           | 0            | 0                     | 0            |
| 2    | 1           | 1            | 2                     | 2            |
| 3    | 0           | 0            | 0                     | 2            |
| 1    | 2           | 1            | 3                     | **3**        |

## Complexity Analysis

- **Time Complexity:** `O(n)` where n is the number of nodes
  - We visit each node exactly once in the DFS traversal
- **Space Complexity:** `O(h)` where h is the height of the tree
  - Due to the recursion stack depth (worst case O(n) for skewed tree)

## Key Insights

1. **Single Pass Solution**: We calculate both the height and diameter in one traversal
2. **Bottom-Up Approach**: Heights are calculated from leaves to root
3. **Global State**: Use nonlocal variable to track maximum across all recursive calls
4. **Path Understanding**: Diameter = edges in longest path = sum of heights of subtrees

## Edge Cases

- **Single Node**: Diameter = 0 (no edges)
- **Linear Tree**: Diameter = n-1 (number of nodes - 1)
- **Balanced Tree**: Diameter passes through root or near root

## Alternative Approaches

1. **Two DFS**: Find farthest node from any node, then find farthest from that node (works for unweighted trees)
2. **BFS Approach**: Level-order traversal with path tracking (less efficient)

![Tree Diameter Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754317738/Screenshot_2025-08-04_195845_spjjmi.png)
