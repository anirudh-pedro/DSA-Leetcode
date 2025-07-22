# 1695. Maximum Erasure Value

## Problem Description

You are given an array of positive integers `nums` and want to erase a subarray containing **unique elements**. The score you get by erasing the subarray is equal to the **sum of its elements**.

Return the **maximum score** you can get by erasing exactly one subarray.

An array `b` is called to be a **subarray** of `a` if it forms a contiguous subsequence of `a`, that is, if it is equal to `a[l], a[l+1], ..., a[r]` for some `(l, r)`.

## Examples

### Example 1:

```
Input: nums = [4,2,4,5,6]
Output: 17
```

**Explanation:**
The optimal subarray here is `[2,4,5,6]`.

### Example 2:

```
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
```

**Explanation:**
The optimal subarray here is `[5,2,1]` or `[1,2,5]`.

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Solution

```python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = nums[0]  # Initialize with first element
        d = defaultdict(int)  # Frequency counter for current window
        l = 0  # Left pointer of sliding window
        s = 0  # Current sum of window

        for i in range(len(nums)):
            # Add current element to window
            d[nums[i]] += 1
            s += nums[i]

            # Shrink window while we have duplicates
            while d[nums[i]] >= 2:
                s -= nums[l]  # Remove left element from sum
                d[nums[l]] -= 1  # Decrease frequency
                if d[nums[l]] == 0:
                    d.pop(nums[l])  # Clean up zero frequencies
                l += 1  # Move left pointer

            # Update maximum sum found
            res = max(res, s)

        return res
```

## Algorithm Explanation

This solution uses the **sliding window technique** to efficiently find the maximum sum subarray with unique elements:

### Step 1: Initialize Variables

- `res`: Tracks the maximum sum found so far
- `d`: Dictionary to count frequency of elements in current window
- `l`: Left pointer of the sliding window
- `s`: Current sum of elements in the window

### Step 2: Expand Window (Right Pointer)

- For each element `nums[i]`, add it to the window
- Increment its frequency in the dictionary
- Add its value to the current sum

### Step 3: Shrink Window (Left Pointer)

- If the current element creates a duplicate (`frequency >= 2`):
  - Remove elements from the left until no duplicates exist
  - Update sum and frequencies accordingly
  - Clean up zero frequencies from dictionary

### Step 4: Update Maximum

- After ensuring the window has unique elements, update the maximum sum
- Continue until all elements are processed

## Step-by-Step Example (nums = [4,2,4,5,6])

| Step | i   | nums[i] | Window  | Sum | Duplicates? | Action     | Result                |
| ---- | --- | ------- | ------- | --- | ----------- | ---------- | --------------------- |
| 1    | 0   | 4       | [4]     | 4   | No          | -          | res = 4               |
| 2    | 1   | 2       | [4,2]   | 6   | No          | -          | res = 6               |
| 3    | 2   | 4       | [4,2,4] | 10  | Yes (4)     | Remove 4,2 | Window = [4], Sum = 4 |
| 4    | 3   | 5       | [4,5]   | 9   | No          | -          | res = 9               |
| 5    | 4   | 6       | [4,5,6] | 15  | No          | -          | res = 15              |

Wait, let me recalculate this correctly:

| Step | i   | nums[i] | Window    | Sum | Duplicates? | Action         | Result                  |
| ---- | --- | ------- | --------- | --- | ----------- | -------------- | ----------------------- |
| 1    | 0   | 4       | [4]       | 4   | No          | -              | res = 4                 |
| 2    | 1   | 2       | [4,2]     | 6   | No          | -              | res = 6                 |
| 3    | 2   | 4       | [2,4]     | 10  | Yes (4)     | Remove first 4 | Window = [2,4], Sum = 6 |
| 4    | 3   | 5       | [2,4,5]   | 11  | No          | -              | res = 11                |
| 5    | 4   | 6       | [2,4,5,6] | 17  | No          | -              | res = 17                |

Final Result: **17** (subarray `[2,4,5,6]`)

## Time and Space Complexity

- **Time Complexity**: O(n) - Each element is added once and removed at most once
- **Space Complexity**: O(min(n, k)) where k is the number of unique elements (at most 10^4)

## Key Insights

1. **Sliding Window**: Maintain a dynamic window that always contains unique elements
2. **Two Pointers**: Use left and right pointers to expand and contract the window
3. **Frequency Tracking**: Use a dictionary to efficiently detect duplicates
4. **Greedy Approach**: Always try to maximize the window size while maintaining uniqueness
5. **Efficient Shrinking**: When duplicates are found, shrink from the left until resolved

## Why This Approach Works

- **Optimal Substructure**: The maximum unique subarray ending at position `i` can be computed from previous positions
- **No Backtracking**: Once we move the left pointer, we never need to go back
- **Single Pass**: We process each element exactly once in the main loop
- **Dynamic Window**: The window automatically adjusts to maintain the unique constraint

## Alternative Approaches

1. **Set-based Sliding Window**: Use a set instead of dictionary (simpler but less information)
2. **Brute Force**: Check all subarrays O(n²) - too slow for given constraints

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1753206206/Screenshot_2025-07-22_231143_nzi8pq.png)
