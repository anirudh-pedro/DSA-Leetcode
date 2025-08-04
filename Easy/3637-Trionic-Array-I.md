# 3637. Trionic Array I

## Problem Description

You are given an integer array `nums` of length `n`.

An array is **trionic** if there exist indices `0 < p < q < n − 1` such that:

1. `nums[0...p]` is **strictly increasing**
2. `nums[p...q]` is **strictly decreasing**
3. `nums[q...n − 1]` is **strictly increasing**

Return `true` if `nums` is trionic, otherwise return `false`.

## Examples

### Example 1:

```
Input: nums = [1,3,5,4,2,6]
Output: true
```

**Explanation:**
Pick p = 2, q = 4:

- `nums[0...2] = [1, 3, 5]` is strictly increasing (1 < 3 < 5)
- `nums[2...4] = [5, 4, 2]` is strictly decreasing (5 > 4 > 2)
- `nums[4...5] = [2, 6]` is strictly increasing (2 < 6)

### Example 2:

```
Input: nums = [2,1,3]
Output: false
```

**Explanation:**
There is no way to pick p and q to form the required three segments.

## Constraints

- `3 <= n <= 100`
- `-1000 <= nums[i] <= 1000`

## Solution

```python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        flag = [-1, -1]  # [p, q] - transition points

        # Step 1: Find first decreasing point (end of increasing segment)
        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:  # Found first non-increasing pair
                flag[0] = i  # This is point p
                break

        # Validate p: must exist and not be at index 0
        if flag[0] == -1 or flag[0] == 0:
            return False

        # Step 2: Find first increasing point after p (end of decreasing segment)
        for i in range(flag[0], n - 1):
            if nums[i] <= nums[i + 1]:  # Found first non-decreasing pair
                flag[1] = i  # This is point q
                break

        # Validate q: must exist and be different from p
        if flag[1] == -1 or flag[1] == flag[0]:
            return False

        # Step 3: Validate all three segments

        # Segment 1: [0...p] must be strictly increasing
        for i in range(flag[0]):
            if nums[i] >= nums[i + 1]:  # Not strictly increasing
                return False

        # Segment 2: [p...q] must be strictly decreasing
        for i in range(flag[0], flag[1]):
            if nums[i] <= nums[i + 1]:  # Not strictly decreasing
                return False

        # Segment 3: [q...n-1] must be strictly increasing
        for i in range(flag[1], len(nums) - 1):
            if nums[i] >= nums[i + 1]:  # Not strictly increasing
                return False

        return True
```

## Algorithm Explanation

This solution uses a **three-phase approach** to identify and validate trionic structure:

### Step 1: Find Transition Point p

- Scan from left to right to find the first position where `nums[i] >= nums[i+1]`
- This marks the end of the first increasing segment
- Point `p` must exist and be greater than 0 for valid trionic array

### Step 2: Find Transition Point q

- Starting from point `p`, scan to find the first position where `nums[i] <= nums[i+1]`
- This marks the end of the decreasing segment
- Point `q` must exist and be different from `p`

### Step 3: Validate All Segments

- **Segment 1** `[0...p]`: Verify strictly increasing
- **Segment 2** `[p...q]`: Verify strictly decreasing
- **Segment 3** `[q...n-1]`: Verify strictly increasing

## Step-by-Step Example (nums = [1,3,5,4,2,6])

### Phase 1: Find p

| Index | Value | Comparison | Action    |
| ----- | ----- | ---------- | --------- |
| 0     | 1     | 1 < 3      | Continue  |
| 1     | 3     | 3 < 5      | Continue  |
| 2     | 5     | 5 ≥ 4      | **p = 2** |

### Phase 2: Find q

| Index | Value | Comparison | Action    |
| ----- | ----- | ---------- | --------- |
| 2     | 5     | 5 > 4      | Continue  |
| 3     | 4     | 4 > 2      | Continue  |
| 4     | 2     | 2 ≤ 6      | **q = 4** |

### Phase 3: Validate Segments

| Segment | Range | Values  | Check | Valid? |
| ------- | ----- | ------- | ----- | ------ |
| 1       | [0,2] | [1,3,5] | 1<3<5 | ✓      |
| 2       | [2,4] | [5,4,2] | 5>4>2 | ✓      |
| 3       | [4,5] | [2,6]   | 2<6   | ✓      |

**Result**: `true` (all segments satisfy trionic conditions)

## Trionic Structure Visualization

```
Array: [1, 3, 5, 4, 2, 6]
Index:  0  1  2  3  4  5

       5 ←--- Peak
      /|\
     3 | 4
    /  |  \
   1   |   2
       |    \
       |     6
       |
     p=2   q=4

Segments:
- Increasing: [0,2] → [1,3,5]
- Decreasing: [2,4] → [5,4,2]
- Increasing: [4,5] → [2,6]
```

## Edge Case Analysis

### Invalid Cases:

1. **No decreasing segment**: `[1,2,3,4,5]` - flag[0] = -1
2. **No second increasing segment**: `[1,3,2,1]` - flag[1] = -1
3. **Decreasing starts at index 0**: `[5,4,3,1,2]` - flag[0] = 0
4. **Same transition points**: `[1,2,1,3]` - flag[0] = flag[1]

### Boundary Conditions:

- **Minimum length**: n ≥ 3 required for trionic structure
- **Transition points**: 0 < p < q < n-1 must be satisfied

## Time and Space Complexity

- **Time Complexity**: O(n)
  - O(n) to find transition points p and q
  - O(n) to validate all three segments
  - Total: O(n)
- **Space Complexity**: O(1) - Only using constant extra space

## Key Insights

1. **Greedy Transition Detection**: Find first violation points for segment boundaries
2. **Three-Segment Validation**: Separately verify each segment's monotonicity
3. **Strict Inequalities**: All comparisons must be strict (< or >)
4. **Boundary Constraints**: Transition points must satisfy position requirements
5. **Early Termination**: Return false immediately on any validation failure

## Why This Approach Works

- **Systematic Detection**: Finds natural breakpoints in the array structure
- **Complete Validation**: Ensures all segments meet strict monotonicity requirements
- **Efficient Implementation**: Single pass to find transitions, single pass to validate
- **Handles Edge Cases**: Proper validation of boundary conditions and special cases

## Alternative Approaches

1. **Brute Force**: Try all possible (p,q) pairs - O(n³) time complexity
2. **Dynamic Programming**: Track state transitions - more complex implementation
3. **Peak Detection**: Find local maxima/minima - similar complexity but different logic

## Edge Cases Handled

1. **Arrays too short**: n < 3 automatically returns false
2. **No valid transitions**: Missing p or q points
3. **Invalid segment boundaries**: p or q at invalid positions
4. **Non-strict monotonicity**: Equal adjacent elements in any segment

## Pattern Recognition

This problem is a variation of:

- **Bitonic arrays**: Mountain-like structures with one peak
- **Peak detection**: Finding local maxima in sequences
- **Monotonicity validation**: Checking increasing/decreasing patterns

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754317470/Screenshot_2025-08-04_195412_yxt5bk.png)
