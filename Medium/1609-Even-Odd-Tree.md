# 1609. Even Odd Tree

## Problem Description

A binary tree is named **Even-Odd** if it meets the following conditions:

1. The root of the binary tree is at **level index 0**, its children are at **level index 1**, their children are at **level index 2**, etc.

2. For every **even-indexed level**, all nodes at the level have **odd integer values** in **strictly increasing order** (from left to right).

3. For every **odd-indexed level**, all nodes at the level have **even integer values** in **strictly decreasing order** (from left to right).

Given the root of a binary tree, return `true` if the binary tree is Even-Odd, otherwise return `false`.

## Examples

### Example 1:

```
Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
```

**Explanation:**
The node values on each level are:

- Level 0: [1] (odd values, increasing)
- Level 1: [10,4] (even values, decreasing)
- Level 2: [3,7,9] (odd values, increasing)
- Level 3: [12,8,6,2] (even values, decreasing)

Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

### Example 2:

```
Input: root = [5,4,2,3,3,7]
Output: false
```

**Explanation:**
The node values on each level are:

- Level 0: [5]
- Level 1: [4,2]
- Level 2: [3,3,7]

Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.

### Example 3:

```
Input: root = [5,9,1,3,5,7]
Output: false
```

**Explanation:**
Node values in the level 1 should be even integers.

## Constraints

- The number of nodes in the tree is in the range `[1, 10^5]`
- `1 <= Node.val <= 10^6`

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0

        while queue:
            level_values = []  # Track values at current level

            # Process all nodes at current level
            for i in range(len(queue)):
                node = queue.popleft()

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                # Check parity requirement for current level
                if level % 2 == 0:  # Even level
                    # Must have odd values
                    if node.val % 2 == 0:
                        return False
                else:  # Odd level
                    # Must have even values
                    if node.val % 2 != 0:
                        return False

                # Check ordering requirement
                if level_values:  # Not the first node in this level
                    if level % 2 == 0:  # Even level: strictly increasing
                        if level_values[-1] >= node.val:
                            return False
                    else:  # Odd level: strictly decreasing
                        if level_values[-1] <= node.val:
                            return False

                level_values.append(node.val)

            level += 1

        return True
```

## Algorithm Explanation

This solution uses **Level-Order Traversal (BFS)** to validate Even-Odd tree properties:

### Step 1: Level-by-Level Processing

- Use BFS to process nodes level by level
- Track current level index to determine requirements
- Process all nodes at current level before moving to next

### Step 2: Validate Parity Requirements

- **Even levels (0, 2, 4, ...)**: All values must be **odd**
- **Odd levels (1, 3, 5, ...)**: All values must be **even**
- Return `false` immediately if any node violates parity requirement

### Step 3: Validate Ordering Requirements

- **Even levels**: Values must be in **strictly increasing** order (left to right)
- **Odd levels**: Values must be in **strictly decreasing** order (left to right)
- Compare each node with the previous node in the same level

### Step 4: Return Result

- If all levels pass both parity and ordering checks, return `true`
- Any violation results in immediate `false` return

## Level Requirements Summary

| Level Type | Level Index | Value Parity | Ordering            |
| ---------- | ----------- | ------------ | ------------------- |
| Even       | 0, 2, 4...  | Odd values   | Strictly Increasing |
| Odd        | 1, 3, 5...  | Even values  | Strictly Decreasing |

## Step-by-Step Example (root = [1,10,4,3,null,7,9,12,8,6,null,null,2])

### Tree Structure:

```
       1
      / \
    10   4
   /   / | \
  3   7  9  null
 / \ / \   \
12 8 6 null 2
```

### Level-by-Level Validation:

| Level    | Nodes      | Values     | Parity Check | Ordering Check                | Valid? |
| -------- | ---------- | ---------- | ------------ | ----------------------------- | ------ |
| 0 (Even) | [1]        | [1]        | 1 is odd ✓   | Single node ✓                 | ✓      |
| 1 (Odd)  | [10,4]     | [10,4]     | Both even ✓  | 10 > 4 (decreasing) ✓         | ✓      |
| 2 (Even) | [3,7,9]    | [3,7,9]    | All odd ✓    | 3 < 7 < 9 (increasing) ✓      | ✓      |
| 3 (Odd)  | [12,8,6,2] | [12,8,6,2] | All even ✓   | 12 > 8 > 6 > 2 (decreasing) ✓ | ✓      |

**Result**: `true` (all levels satisfy Even-Odd properties)

## Validation Logic Details

### Parity Validation:

```python
if level % 2 == 0:  # Even level
    if node.val % 2 == 0:  # Even value on even level
        return False
else:  # Odd level
    if node.val % 2 != 0:  # Odd value on odd level
        return False
```

### Ordering Validation:

```python
if level_values:  # Not the first node
    if level % 2 == 0:  # Even level: increasing
        if level_values[-1] >= node.val:  # Not strictly increasing
            return False
    else:  # Odd level: decreasing
        if level_values[-1] <= node.val:  # Not strictly decreasing
            return False
```

## Time and Space Complexity

- **Time Complexity**: O(n) - Visit each node exactly once
- **Space Complexity**: O(w) where w is the maximum width of the tree
  - BFS queue can contain at most one complete level
  - level_values array stores at most one level's worth of values

## Key Insights

1. **Level-Order Traversal**: BFS naturally processes nodes level by level
2. **Immediate Validation**: Check constraints as we process each node
3. **Early Termination**: Return false as soon as any constraint is violated
4. **State Tracking**: Track current level and previous values for ordering checks
5. **Parity Logic**: Use modulo operations to determine even/odd for both levels and values

## Why This Approach Works

- **Systematic Processing**: BFS ensures we process complete levels before moving on
- **Efficient Validation**: Check both parity and ordering in single pass
- **Memory Efficient**: Only store current level's values, not entire tree
- **Early Exit**: Stop processing as soon as violation is found

## Edge Cases Handled

1. **Single Node Tree**: Root at level 0 must be odd (handled correctly)
2. **Two Node Tree**: Root and one child (validates both levels)
3. **Duplicate Values**: Strictly increasing/decreasing means no duplicates allowed
4. **Large Values**: Algorithm works regardless of value magnitude

## Alternative Approaches

1. **Recursive DFS**: Could use recursion with level parameter, but BFS is more natural
2. **Two-Pass**: First collect all levels, then validate (uses more memory)
3. **Level Collection**: Store all levels first, then validate each (less efficient)

## Optimization Notes

- **Space Optimization**: Could avoid storing level_values by comparing with previous node directly
- **Early Termination**: Algorithm already optimized to return false immediately on violation
- **Cache Efficiency**: BFS has good cache locality compared to DFS for this problem

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754317326/Screenshot_2025-08-04_195045_cfdbrr.png)
