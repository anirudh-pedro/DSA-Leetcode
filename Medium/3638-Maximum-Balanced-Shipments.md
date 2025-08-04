# 3638. Maximum Balanced Shipments

## Problem Description

You are given an integer array `weight` of length `n`, representing the weights of `n` parcels arranged in a straight line. A **shipment** is defined as a contiguous subarray of parcels. A shipment is considered **balanced** if the weight of the last parcel is **strictly less** than the maximum weight among all parcels in that shipment.

Select a set of **non-overlapping, contiguous, balanced shipments** such that each parcel appears in at most one shipment (parcels may remain unshipped).

Return the **maximum possible number** of balanced shipments that can be formed.

## Examples

### Example 1:

```
Input: weight = [2,5,1,4,3]
Output: 2
```

**Explanation:**
We can form the maximum of two balanced shipments as follows:

**Shipment 1**: `[2, 5, 1]`

- Maximum parcel weight = 5
- Last parcel weight = 1, which is strictly less than 5. Thus, it's balanced.

**Shipment 2**: `[4, 3]`

- Maximum parcel weight = 4
- Last parcel weight = 3, which is strictly less than 4. Thus, it's balanced.

It is impossible to partition the parcels to achieve more than two balanced shipments.

### Example 2:

```
Input: weight = [4,4]
Output: 0
```

**Explanation:**
No balanced shipment can be formed:

- A shipment `[4, 4]` has maximum weight 4 and the last parcel's weight is also 4, which is not strictly less. Thus, it's not balanced.
- Single-parcel shipments `[4]` have the last parcel weight equal to the maximum parcel weight, thus not balanced.

## Constraints

- `2 <= n <= 10^5`
- `1 <= weight[i] <= 10^9`

## Solution

```python
class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        current_shipment = []  # Current shipment being built
        max_weight = float('-inf')  # Maximum weight in current shipment
        balanced_count = 0  # Count of balanced shipments found

        for i in range(len(weight)):
            # Add current parcel to the shipment
            current_shipment.append(weight[i])

            # Update maximum weight in current shipment
            if max_weight < current_shipment[-1]:
                max_weight = current_shipment[-1]

            # Check if we can form a balanced shipment
            if len(current_shipment) > 1:  # Need at least 2 parcels
                # Check if last parcel weight < maximum weight
                if current_shipment[-1] < max_weight:
                    balanced_count += 1  # Found a balanced shipment
                    current_shipment = []  # Reset for next shipment
                    max_weight = float('-inf')  # Reset maximum

        return balanced_count
```

## Algorithm Explanation

This solution uses a **greedy approach** to maximize the number of balanced shipments:

### Step 1: Build Shipments Incrementally

- Process parcels from left to right
- Add each parcel to the current shipment being built
- Track the maximum weight seen so far in the current shipment

### Step 2: Check Balanced Condition

- For shipments with at least 2 parcels, check if the last parcel's weight is strictly less than the maximum weight
- **Balanced condition**: `last_weight < max_weight`

### Step 3: Greedy Decision Making

- As soon as a balanced shipment is found, immediately "ship" it
- Reset and start building a new shipment from the next parcel
- This greedy approach maximizes the number of shipments

### Step 4: Continue Until End

- Process all parcels, forming balanced shipments whenever possible
- Return the total count of balanced shipments formed

## Step-by-Step Example (weight = [2,5,1,4,3])

| Step | Parcel | Current Shipment | Max Weight | Last < Max?  | Action    | Count |
| ---- | ------ | ---------------- | ---------- | ------------ | --------- | ----- |
| 1    | 2      | [2]              | 2          | N/A (size=1) | Continue  | 0     |
| 2    | 5      | [2,5]            | 5          | 5 ≮ 5        | Continue  | 0     |
| 3    | 1      | [2,5,1]          | 5          | 1 < 5 ✓      | **Ship!** | 1     |
| 4    | 4      | [4]              | 4          | N/A (size=1) | Continue  | 1     |
| 5    | 3      | [4,3]            | 4          | 3 < 4 ✓      | **Ship!** | 2     |

**Result**: 2 balanced shipments formed

## Balanced Shipment Conditions

### Required Conditions:

1. **Size**: Shipment must contain at least 2 parcels
2. **Balance**: Last parcel weight **<** maximum weight in shipment
3. **Contiguous**: Parcels must be consecutive in the original array

### Invalid Cases:

- **Single parcel**: `[x]` → last weight = max weight (not strictly less)
- **Non-decreasing end**: `[1,2,3]` → last weight = max weight
- **Equal weights**: `[4,4]` → last weight = max weight

## Why Greedy Approach Works

### Optimal Substructure:

- Once we find a balanced shipment, it's always optimal to "ship" it immediately
- Waiting longer can only reduce future opportunities (no benefit)

### Greedy Choice Property:

- Taking the earliest balanced shipment doesn't prevent optimal solutions for remaining parcels
- Each balanced shipment is independent of others (non-overlapping constraint)

### Example of Greedy Optimality:

```
Array: [2,5,1,4,3]

Greedy: [2,5,1] + [4,3] = 2 shipments ✓

Alternative: [2,5,1,4] (not balanced: 4 ≮ 5) = 0 shipments ✗
```

## Time and Space Complexity

- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(k) where k is the maximum shipment size
  - In practice, k is typically small, so effectively O(1) space

## Key Insights

1. **Greedy Strategy**: Ship balanced shipments as soon as they're found
2. **Maximum Tracking**: Maintain running maximum for balance checking
3. **Early Shipping**: Don't wait for potentially larger shipments
4. **Non-overlapping**: Each parcel used at most once
5. **Contiguous Requirement**: Only consider consecutive parcels

## Why This Approach Works

- **Maximizes Opportunities**: Greedy approach ensures we don't miss any valid shipments
- **Optimal Decisions**: Taking earliest balanced shipment is always optimal
- **Simple Logic**: Clear conditions for when to form a shipment
- **Efficient Implementation**: Single pass with constant space

## Edge Cases Handled

1. **All Equal Weights**: `[3,3,3,3]` → No balanced shipments possible
2. **Strictly Increasing**: `[1,2,3,4]` → No balanced shipments possible
3. **Single Peak**: `[1,5,2]` → One balanced shipment `[1,5,2]`
4. **Multiple Peaks**: `[1,3,2,5,1]` → Two balanced shipments

## Alternative Approaches

1. **Dynamic Programming**: O(n²) time - overkill for this greedy problem
2. **Brute Force**: O(n³) - check all possible combinations
3. **Segment Tree**: Complex data structure not needed for this linear problem

## Pattern Recognition

This problem involves:

- **Greedy algorithms**: Making locally optimal choices
- **Subarray problems**: Working with contiguous segments
- **Optimization**: Maximizing count under constraints
- **Peak detection**: Finding local maxima patterns

![Algorithm Visualization](https://res.cloudinary.com/dfo6ngde0/image/upload/v1754317604/Screenshot_2025-08-04_195629_wqxjlq.png)
