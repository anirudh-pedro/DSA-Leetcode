# 2583. Kth Largest Sum in a Binary Tree

## Problem Description

You are given the **root** of a binary tree and a positive integer **k**.

The **level sum** in the tree is the sum of the values of the nodes that are on the same level.

Return the **kth largest level sum** in the tree (not necessarily distinct). If there are fewer than **k levels** in the tree, return **-1**.

**Note**: Two nodes are on the same level if they have the same distance from the root.

## Examples

### Example 1:

```
Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
```

**Explanation:**
The level sums are the following:

- Level 1: 5
- Level 2: 8 + 9 = 17
- Level 3: 2 + 1 + 3 + 7 = 13
- Level 4: 4 + 6 = 10

The 2nd largest level sum is 13.

### Example 2:

```
Input: root = [1,2,null,3], k = 1
Output: 3
```

**Explanation:**
The largest level sum is 3.

## Constraints

- The number of nodes in the tree is `n`
- `2 <= n <= 10^5`
- `1 <= Node.val <= 10^6`
- `1 <= k <= n`

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        heap = []  # Min-heap to maintain k largest sums

        while queue:
            level_nodes = []
            # Process all nodes at current level
            for i in range(len(queue)):
                node = queue.popleft()
                level_nodes.append(node.val)

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate current level sum
            level_sum = sum(level_nodes)

            # Maintain heap of size k with largest sums
            heapq.heappush(heap, level_sum)
            if len(heap) > k:
                heapq.heappop(heap)  # Remove smallest sum

        # Return kth largest sum if we have k levels, else -1
        return heap[0] if len(heap) == k else -1
```

## Algorithm Explanation

This solution combines **Level-Order Traversal (BFS)** with a **Min-Heap** to efficiently find the kth largest level sum:

### Step 1: Level-Order Traversal

- Use BFS to traverse the tree level by level
- For each level, collect all node values and calculate the sum
- Process all nodes at the current level before moving to the next

### Step 2: Maintain K Largest Sums

- Use a min-heap of size k to track the k largest level sums
- For each level sum:
  - Add it to the heap
  - If heap size exceeds k, remove the smallest element
- This ensures the heap always contains the k largest sums seen so far

### Step 3: Return Result

- If we have exactly k levels, return the minimum element in the heap (kth largest)
- If we have fewer than k levels, return -1

## Step-by-Step Example (root = [5,8,9,2,1,3,7,4,6], k = 2)

### Tree Structure:

```
        5
      /   \
     8     9
   /  \   / \
  2    1 3   7
 / \
4   6
```

### Level-by-Level Processing:

| Level | Nodes     | Values    | Sum | Heap State | Action                       |
| ----- | --------- | --------- | --- | ---------- | ---------------------------- |
| 1     | [5]       | [5]       | 5   | [5]        | Add 5                        |
| 2     | [8,9]     | [8,9]     | 17  | [5,17]     | Add 17                       |
| 3     | [2,1,3,7] | [2,1,3,7] | 13  | [13,17]    | Add 13, remove 5             |
| 4     | [4,6]     | [4,6]     | 10  | [13,17]    | Add 10, remove 10 (size > k) |

**Final Heap**: [13, 17] → **2nd largest** = 13

## Heap Management Details

The key insight is using a **min-heap of size k**:

### Why Min-Heap?

- **Root = Smallest**: In a min-heap of k largest elements, the root is the kth largest
- **Efficient Removal**: We can easily remove the smallest when heap exceeds size k
- **O(log k) Operations**: Both insertion and removal are logarithmic in k

### Heap Size Management:

```python
if len(heap) > k:
    heapq.heappop(heap)  # Remove smallest (maintain size k)
```

This ensures:

- Heap contains at most k elements
- All elements in heap are among the k largest seen
- Root of heap is the kth largest element

## Time and Space Complexity

- **Time Complexity**: O(n + L log k)
  - O(n) for BFS traversal of all nodes
  - O(L log k) for heap operations, where L = number of levels ≤ log n
  - Total: O(n + log n × log k) = O(n)
- **Space Complexity**: O(w + k)
  - O(w) for BFS queue, where w = maximum width of tree
  - O(k) for the heap

## Key Insights

1. **Level-Order Traversal**: BFS naturally processes nodes level by level
2. **Min-Heap Strategy**: Efficiently maintains k largest elements with O(log k) operations
3. **Space Optimization**: Only store k sums instead of all level sums
4. **Early Termination**: Could stop early if we know we have fewer than k levels
5. **Boundary Handling**: Return -1 when insufficient levels exist

## Why This Approach Works

- **Correctness**: BFS guarantees level-by-level processing
- **Efficiency**: Min-heap of size k is more efficient than sorting all level sums
- **Memory Optimal**: O(k) space for sums instead of O(L) where L could be large
- **Scalability**: Works well even for large trees with many levels

## Alternative Approaches

1. **Collect All + Sort**: O(L log L) time, O(L) space - simpler but less efficient
2. **Max-Heap**: Could use max-heap and extract k elements, but more complex
3. **Quick Select**: O(L) average time for kth largest, but O(L) space needed

## Edge Cases Handled

1. **k > number of levels**: Returns -1
2. **k = 1**: Returns the maximum level sum
3. **Single level tree**: Works correctly
4. **All levels have same sum**: Returns the sum (handles non-distinct requirement)

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754154046/Screenshot_2025-08-02_222811_a1hcjm.png)
