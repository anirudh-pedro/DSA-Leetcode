# 904. Fruit Into Baskets

**Difficulty:** Medium  
**Topics:** Array, Hash Table, Sliding Window  
**Companies:** Amazon, Google, Facebook

## Problem Description

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `ith` tree produces.

You want to **collect as much fruit as possible**. However, the owner has some strict rules that you must follow:

1. You only have **two baskets**, and each basket can only hold a **single type of fruit**. There is no limit on the amount of fruit each basket can hold.
2. Starting from any tree of your choice, you must pick **exactly one fruit from every tree** (including the start tree) while **moving to the right**. The picked fruits must fit in one of your baskets.
3. Once you reach a tree with fruit that **cannot fit in your baskets**, you must **stop**.

Given the integer array `fruits`, return the **maximum number of fruits** you can pick.

## Examples

### Example 1:

```
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
```

### Example 2:

```
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
```

### Example 3:

```
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
```

## Constraints

- `1 <= fruits.length <= 10^5`
- `0 <= fruits[i] < fruits.length`

## Solution

```python
from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Early optimization: if 2 or fewer unique fruits, collect all
        if len(set(fruits)) <= 2:
            return len(fruits)

        # Dictionary to count fruit types in current window
        fruit_count = defaultdict(int)
        left = 0  # Left pointer of sliding window
        max_fruits = 0  # Maximum fruits collected

        # Sliding window approach
        for right in range(len(fruits)):
            # Add current fruit to the window
            fruit_count[fruits[right]] += 1

            # Shrink window while we have more than 2 fruit types
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                # Remove fruit type if count becomes 0
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1

            # Update maximum when we have exactly 2 fruit types
            if len(fruit_count) == 2:
                max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
```

## Algorithm Explanation

This solution uses the **sliding window technique** to find the longest subarray with at most 2 distinct elements:

### Key Insight

- **Problem Translation**: Find the longest contiguous subarray with at most 2 distinct fruit types
- **Sliding Window**: Expand right boundary and shrink left boundary to maintain valid window
- **Hash Map Counting**: Track frequency of each fruit type in current window

### Step-by-Step Process

1. **Window Expansion**: Move right pointer to include new fruits
2. **Constraint Checking**: If more than 2 fruit types, shrink from left
3. **Window Management**: Remove fruit types when their count becomes 0
4. **Maximum Tracking**: Update result when window has exactly 2 fruit types

### Example Walkthrough

For input `[1,2,3,2,2]`:

| Step | Right | Left | Window    | Fruit Count   | Valid? | Max Fruits |
| ---- | ----- | ---- | --------- | ------------- | ------ | ---------- |
| 1    | 0     | 0    | [1]       | {1:1}         | ✓      | 0          |
| 2    | 1     | 0    | [1,2]     | {1:1,2:1}     | ✓      | 2          |
| 3    | 2     | 0    | [1,2,3]   | {1:1,2:1,3:1} | ✗      | 2          |
| 4    | 2     | 1    | [2,3]     | {2:1,3:1}     | ✓      | 2          |
| 5    | 3     | 1    | [2,3,2]   | {2:2,3:1}     | ✓      | 3          |
| 6    | 4     | 1    | [2,3,2,2] | {2:3,3:1}     | ✓      | **4**      |

**Final Result**: 4 (subarray [2,3,2,2])

## Complexity Analysis

- **Time Complexity:** `O(n)` where n is the length of fruits array
  - Each element is visited at most twice (once by right pointer, once by left pointer)
- **Space Complexity:** `O(1)` since we store at most 3 fruit types in the hash map

## Key Insights

1. **Sliding Window Pattern**: Classic technique for subarray problems with constraints
2. **Hash Map for Counting**: Efficiently track fruit type frequencies
3. **Window Validity**: Maintain exactly 2 fruit types for maximum collection
4. **Early Optimization**: Handle edge case where total unique fruits ≤ 2

## Edge Cases

- **All Same Fruit**: Return total length (1 basket needed)
- **Only 2 Fruit Types**: Return total length (fits in 2 baskets)
- **Single Fruit**: Return 1
- **Alternating Pattern**: May require careful window management

## Alternative Approaches

1. **Two Pointers with Last Position Tracking**: Track last occurrence of each fruit type
2. **Brute Force**: Try all possible starting positions (O(n²))
3. **Optimized Sliding Window**: Use fixed-size hash map for better space efficiency

![Fruit Into Baskets Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754318195/Screenshot_2025-08-04_200621_hrtmbd.png)
